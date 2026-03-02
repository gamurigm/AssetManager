import asyncio
import json
import os
import sys
import subprocess
import pandas as pd
from pathlib import Path


# ─── Worker script (kept alive in memory — no re-import overhead) ────────────
_WORKER_SCRIPT = r'''
import sys, json, traceback

# One-time heavy imports (done once at worker startup)
try:
    import pandas as pd
    from openbb import obb
    sys.stderr.write("[OpenBB Worker] Ready.\n")
    sys.stderr.flush()
except Exception as e:
    sys.stderr.write(f"[OpenBB Worker] INIT ERROR: {e}\n")
    sys.stderr.flush()
    sys.exit(1)

def _format_dict(d, indent=0):
    lines = []
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, float):
            lines.append(f"{prefix}{k}: {v:,.4f}")
        elif isinstance(v, int):
            lines.append(f"{prefix}{k}: {v:,}")
        else:
            lines.append(f"{prefix}{k}: {v}")
    return "\n".join(lines)

def handle(request):
    path_parts = request["path_parts"]
    kwargs = request.get("kwargs", {})

    obj = obb
    for attr in path_parts:
        if not hasattr(obj, attr):
            available = [a for a in dir(obj) if not a.startswith("_")]
            return {"error": f"'{attr}' not found. Available: {', '.join(available[:15])}"}
        obj = getattr(obj, attr)

    res = obj(**kwargs)

    if hasattr(res, "to_dataframe"):
        df = res.to_dataframe()
        if df.empty:
            return {"output": "Query returned no data."}
        text = df.head(25).to_string(index=False)
        if len(df) > 25:
            text += f"\n... Showing 25 of {len(df)} rows"
        return {"output": text}
    elif hasattr(res, "results"):
        results = res.results
        if isinstance(results, list):
            if len(results) == 0:
                return {"output": "Query returned no results."}
            elif hasattr(results[0], "__dict__"):
                lines = [str(r.__dict__ if hasattr(r, "__dict__") else r) for r in results[:20]]
                text = "\n".join(lines)
                if len(results) > 20:
                    text += f"\n... Showing 20 of {len(results)} results"
                return {"output": text}
            else:
                return {"output": str(results[:20])}
        else:
            return {"output": _format_dict(results) if isinstance(results, dict) else str(results)}
    else:
        return {"output": str(res)}

# Main loop: read JSON lines from stdin, write JSON lines to stdout
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        request = json.loads(line)
        result = handle(request)
    except Exception as e:
        result = {"error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result) + "\n")
    sys.stdout.flush()
'''


class OpenBBNativeService:
    """
    Persistent worker that keeps OpenBB loaded in memory.
    First command warms up the interpreter (~3s), all subsequent commands
    execute in <500ms since imports are already cached.
    """

    def __init__(self, openbb_dir: str = r"C:\AssetManager\external_repos\OpenBB\OpenBB"):
        self.openbb_dir = openbb_dir
        self.openbb_python = os.path.join(self.openbb_dir, ".venv", "Scripts", "python.exe")
        self._worker: subprocess.Popen | None = None
        self._lock = asyncio.Lock()

    def exists(self) -> bool:
        return os.path.exists(self.openbb_python)

    def _ensure_worker(self):
        """Start the persistent worker process if not already running."""
        if self._worker is not None and self._worker.poll() is None:
            return  # Already alive
        self._worker = subprocess.Popen(
            [self.openbb_python, "-c", _WORKER_SCRIPT],
            cwd=self.openbb_dir,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # line-buffered
        )

    async def execute(self, command_path: str, kwargs: dict) -> dict:
        """
        Executes an OpenBB command via the persistent worker process.
        Falls back to one-shot subprocess if the worker is unavailable.
        """
        if not self.exists():
            return {"error": "Native OpenBB python not found.", "type": "error"}

        path_parts = command_path.split(".")

        # If chart is requested, detach and return immediately
        if kwargs.get('chart'):
            script = self._build_onetime_script(path_parts, kwargs)
            subprocess.Popen([self.openbb_python, "-c", script], cwd=self.openbb_dir)
            return {"output": f"Executing {command_path} natively. Chart window will open shortly."}

        # Try the persistent worker (fast path)
        try:
            return await self._execute_via_worker(path_parts, kwargs)
        except Exception as e:
            print(f"[OpenBBNative] Worker failed ({e}), falling back to subprocess...")
            self._worker = None  # Reset so next call re-creates
            return await self._execute_via_subprocess(path_parts, kwargs)

    async def _execute_via_worker(self, path_parts: list, kwargs: dict) -> dict:
        """Send a command to the persistent worker and read the response."""
        async with self._lock:  # Serialize access to the worker's stdin/stdout
            self._ensure_worker()
            request = json.dumps({"path_parts": path_parts, "kwargs": kwargs})

            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self._worker_roundtrip, request)
            return result

    def _worker_roundtrip(self, request_json: str) -> dict:
        """Blocking: write request line, read response line."""
        try:
            self._worker.stdin.write(request_json + "\n")
            self._worker.stdin.flush()

            # Read with timeout (30s max)
            import select
            import time
            deadline = time.time() + 30
            response_line = ""

            while time.time() < deadline:
                line = self._worker.stdout.readline()
                if line:
                    response_line = line.strip()
                    break
                if self._worker.poll() is not None:
                    raise RuntimeError("Worker process died")
                time.sleep(0.05)

            if not response_line:
                raise TimeoutError("Worker did not respond within 30s")

            return json.loads(response_line)
        except Exception as e:
            # Kill broken worker
            if self._worker and self._worker.poll() is None:
                self._worker.kill()
            self._worker = None
            raise

    async def _execute_via_subprocess(self, path_parts: list, kwargs: dict) -> dict:
        """Legacy fallback: one-shot subprocess execution."""
        script = self._build_onetime_script(path_parts, kwargs)
        process = await asyncio.create_subprocess_exec(
            self.openbb_python, "-c", script,
            cwd=self.openbb_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        output_str = stdout.decode('utf-8', errors='replace').strip()
        err_str = stderr.decode('utf-8', errors='replace').strip()

        if process.returncode != 0:
            return {"error": err_str or output_str or "Unknown Native Exec Error", "type": "error"}
        return {"output": output_str or "Command processed."}

    def _build_onetime_script(self, path_parts: list, kwargs: dict) -> str:
        return f"""import sys, pandas as pd
from openbb import obb

def _format_dict(d, indent=0):
    lines = []
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, float): lines.append(f"{{prefix}}{{k}}: {{v:,.4f}}")
        elif isinstance(v, int): lines.append(f"{{prefix}}{{k}}: {{v:,}}")
        else: lines.append(f"{{prefix}}{{k}}: {{v}}")
    return "\\n".join(lines)

try:
    obj = obb
    for attr in {repr(path_parts)}:
        if not hasattr(obj, attr):
            available = [a for a in dir(obj) if not a.startswith("_")]
            print(f"Error: '{{attr}}' not found. Available: {{', '.join(available[:15])}}")
            sys.exit(1)
        obj = getattr(obj, attr)
    res = obj(**{repr(kwargs)})
    if hasattr(res, "to_dataframe"):
        df = res.to_dataframe()
        if df.empty: print("Query returned no data.")
        else:
            print(df.head(25).to_string(index=False))
            if len(df) > 25: print(f"\\n... Showing 25 of {{len(df)}} rows")
    elif hasattr(res, "results"):
        results = res.results
        if isinstance(results, list):
            if len(results) == 0: print("Query returned no results.")
            elif hasattr(results[0], "__dict__"):
                lines = [str(r.__dict__ if hasattr(r, "__dict__") else r) for r in results[:20]]
                print("\\n".join(lines))
                if len(results) > 20: print(f"\\n... Showing 20 of {{len(results)}} results")
            else: print(str(results[:20]))
        else: print(_format_dict(results) if isinstance(results, dict) else str(results))
    else: print(str(res))
except Exception as e:
    print(f"Error: {{e}}")
    sys.exit(1)
"""


openbb_native = OpenBBNativeService()


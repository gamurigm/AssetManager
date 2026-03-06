import asyncio
import json
import os
import sys
import subprocess
import pandas as pd
from pathlib import Path


# ─── Worker script (kept alive in memory — no re-import overhead) ────────────
_WORKER_SCRIPT = r'''
import sys, json, traceback, difflib

# One-time heavy imports (done once at worker startup)
try:
    import pandas as pd
    from openbb import obb
    from datetime import datetime, timedelta
    sys.stderr.write("[OpenBB Worker] Ready.\n")
    sys.stderr.flush()
except Exception as e:
    sys.stderr.write(f"[OpenBB Worker] INIT ERROR: {e}\n")
    sys.stderr.flush()
    sys.exit(1)

def _format_dict(d, indent=0):
    if not isinstance(d, dict):
        return str(d)
    lines = []
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, float):
            lines.append(f"{prefix}{k}: {v:,.4f}")
        elif isinstance(v, int):
            lines.append(f"{prefix}{k}: {v:,}")
        elif isinstance(v, dict):
            lines.append(f"{prefix}{k}:\n{_format_dict(v, indent+1)}")
        else:
            lines.append(f"{prefix}{k}: {v}")
    return "\n".join(lines)

def handle(request):
    try:
        path_parts = request["path_parts"]
        kwargs = request.get("kwargs", {})

        # ── Technical & Quantitative indicators: auto-fetch OHLCV data first ──────────
        is_technical = path_parts[0] == "technical" if path_parts else False
        is_quantitative = path_parts[0] == "quantitative" if path_parts else False
        is_relative_rotation = is_technical and len(path_parts) > 1 and path_parts[1] == "relative_rotation"

        if is_relative_rotation:
            # relative_rotation needs ALL symbols + benchmark fetched and stacked into
            # a single DataFrame with a "symbol" column. Benchmark MUST be present.
            raw_symbols = kwargs.pop("symbol", "AAPL,MSFT,NVDA")
            benchmark = kwargs.get("benchmark", "SPY")
            _default_start = (datetime.today() - timedelta(days=730)).strftime("%Y-%m-%d")  # 2 years
            start_date = kwargs.pop("start_date", _default_start)
            kwargs.pop("end_date", None)
            kwargs.pop("provider", None)

            # Parse symbol list, ensure benchmark is included
            sym_list = [s.strip() for s in str(raw_symbols).split(",") if s.strip()]
            if benchmark not in sym_list:
                sym_list.append(benchmark)

            frames = []
            failed_syms = []
            for sym in sym_list:
                try:
                    hist = obb.equity.price.historical(symbol=sym, start_date=start_date, provider="yfinance")
                    df_sym = hist.to_dataframe().reset_index()
                    df_sym["symbol"] = sym
                    frames.append(df_sym)
                except Exception as e:
                    failed_syms.append(f"{sym} ({str(e)})")

            if not frames:
                return {"error": f"Failed to fetch data for ALL symbols. Detailed failures: {', '.join(failed_syms)}"}
            
            if failed_syms:
                # Some failed, some succeeded. We can proceed but should ideally warn.
                # However, for RRG, if symbols are missing it might crash later.
                pass

            combined = pd.concat(frames, ignore_index=True)
            kwargs["data"] = combined
            # Pass symbols list (without benchmark — it's passed separately via benchmark=)
            user_syms = [s for s in sym_list if s != benchmark]
            if user_syms:
                kwargs["symbols"] = user_syms
            
            # Check if all user_syms are in the combined data
            present_syms = combined["symbol"].unique()
            missing = [s for s in user_syms if s not in present_syms]
            if missing:
                 return {"error": f"Required data missing for symbols: {', '.join(missing)}. Please check tickers (e.g. use ^DJI instead of DJI).", "hint": "YFinance tickers usually require ^ for indices."}

        elif is_technical or is_quantitative:
            symbol = kwargs.pop("symbol", "SPY")
            # Increase default lookback to 2 years to satisfy 252-day windows for sharpe/risk metrics
            _default_start = (datetime.today() - timedelta(days=730)).strftime("%Y-%m-%d")
            start_date = kwargs.pop("start_date", _default_start)
            kwargs.pop("end_date", None)
            kwargs.pop("provider", None)
            try:
                hist = obb.equity.price.historical(symbol=symbol, start_date=start_date, provider="yfinance")
                df = hist.to_dataframe().reset_index()
            except Exception as e:
                return {"error": f"Failed to fetch data for {symbol}: {str(e)}", "traceback": traceback.format_exc()}
            kwargs["data"] = df
            
            # Default target to 'close' for quantitative stats if not provided
            if is_quantitative and "target" not in kwargs:
                kwargs["target"] = "close"

        obj = obb
        for i, attr in enumerate(path_parts):
            if not hasattr(obj, attr):
                available = [a for a in dir(obj) if not a.startswith("_")]
                matches = difflib.get_close_matches(attr, available)
                error_msg = f"'{attr}' not found at step {i} of {'.'.join(path_parts)}."
                if matches:
                    error_msg += f" Did you mean one of these? {', '.join(matches)}"
                else:
                    error_msg += f" Available at this level: {', '.join(available[:15])}"
                return {"error": error_msg}
            obj = getattr(obj, attr)

        # Detection of OpenBB-specific validation errors if not caught by hasattr/difflib
        res = obj(**kwargs)
    except Exception as e:
        err_type = type(e).__name__
        err_msg = str(e)
        
        # If it looks like a Pydantic error (common in OpenBB 4.x)
        if "validation" in err_msg.lower() or "input should be" in err_msg.lower():
            return {
                "error": f"Validation Error: {err_msg}",
                "traceback": traceback.format_exc(),
                "hint": "Check the 'provider' and mandatory parameters for this endpoint."
            }
        
        return {"error": f"{err_type}: {err_msg}", "traceback": traceback.format_exc()}

    try:
        chart_requested = kwargs.get("chart", False)
        if chart_requested:
            if hasattr(res, "chart") and res.chart is not None:
                if hasattr(res.chart, "fig") and res.chart.fig is not None:
                    html = res.chart.fig.to_html(include_plotlyjs="cdn", full_html=True, config={"scrollZoom": True, "displayModeBar": True})
                    return {"html": html, "type": "chart_window"}
                else:
                    return {"error": "Chart object has no figure."}
            else:
                return {"error": "No chart generated for this command."}

        # Try to_dataframe first, but wrap in try-except for scalar metrics
        if hasattr(res, "to_dataframe"):
            try:
                df = res.to_dataframe()
                if not df.empty:
                    text = df.head(25).to_string(index=False)
                    if len(df) > 25:
                        text += f"\n... Showing 25 of {len(df)} rows"
                    return {"output": text}
                else:
                    return {"output": "Query returned no data."}
            except:
                # Some scalar results fail to_dataframe(), fall through to results
                pass

        if hasattr(res, "results"):
            results = res.results
            if isinstance(results, list):
                if len(results) == 0:
                    return {"output": "Query returned no results."}
                elif len(results) > 0 and hasattr(results[0], "__dict__"):
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
    except Exception as e:
        return {"error": f"Format Error ({type(e).__name__}): {str(e)}", "traceback": traceback.format_exc()}

# Main loop: read JSON lines from stdin, write JSON lines to stdout
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        request = json.loads(line)
        result = handle(request)
    except Exception as e:
        result = {"error": f"JSON ERROR: {e}", "traceback": traceback.format_exc()}
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

    async def _execute_chart_html(self, path_parts: list, kwargs: dict) -> dict:
        """Run the chart command and return full Plotly HTML to open in a new window.
        Uses subprocess.run in a thread for Windows compatibility with uvicorn.
        """
        script = self._build_chart_html_script(path_parts, kwargs)

        def _run_chart_subprocess() -> dict:
            try:
                result = subprocess.run(
                    [self.openbb_python, "-c", script],
                    cwd=self.openbb_dir,
                    capture_output=True,
                    text=True,
                    timeout=90,
                )
                html_output = result.stdout.strip()
                err = result.stderr.strip()
                if result.returncode != 0 or not html_output:
                    msg = err or "No chart output produced"
                    # Strip leading ERROR: prefix if present
                    msg = msg.replace("ERROR: ", "", 1)
                    return {"error": msg, "type": "error"}
                return {"html": html_output, "type": "chart_window"}
            except subprocess.TimeoutExpired:
                return {"error": "Chart generation timed out (90s)", "type": "error"}
            except Exception as e:
                return {"error": f"Chart subprocess error: {type(e).__name__}: {e}", "type": "error"}

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, _run_chart_subprocess)

    def _build_chart_script(self, path_parts: list, kwargs: dict) -> str:
        """Build a script that opens a Plotly chart in the browser via .show() [legacy]."""
        return f"""import sys
from openbb import obb

try:
    obj = obb
    for attr in {repr(path_parts)}:
        if not hasattr(obj, attr):
            print(f"Error: '{{attr}}' not found", file=sys.stderr)
            sys.exit(1)
        obj = getattr(obj, attr)

    res = obj(**{repr(kwargs)})

    # Try native .show() first (opens browser via Plotly)
    if hasattr(res, "show"):
        res.show()
    elif hasattr(res, "chart") and res.chart and hasattr(res.chart, "fig"):
        res.chart.fig.show()
    else:
        # Fallback: generate chart explicitly if supported
        if hasattr(res, "to_dataframe"):
            df = res.to_dataframe()
            if not df.empty:
                try:
                    import plotly.express as px
                    fig = px.line(df.reset_index(), title="{repr('.'.join(path_parts))}")
                    fig.show()
                except ImportError:
                    pass
except Exception as e:
    print(f"Chart error: {{e}}", file=sys.stderr)
    sys.exit(1)
"""

    def _build_chart_html_script(self, path_parts: list, kwargs: dict) -> str:
        """Build a script that outputs the full Plotly HTML page to stdout."""
        # Technical indicators need OHLCV data fetched first.
        # If the path starts with 'technical', auto-fetch equity historical data.
        is_technical = path_parts[0] == "technical" if path_parts else False

        if is_technical:
            symbol = kwargs.get("symbol", "SPY")
            start_date = kwargs.get("start_date", "2023-01-01")
            # Build kwargs for the indicator without symbol/start_date (not valid params)
            indicator_kwargs = {k: v for k, v in kwargs.items()
                                if k not in ("symbol", "start_date", "end_date", "provider")}
            indicator_kwargs["chart"] = True
            return f"""import sys
from openbb import obb

try:
    # Step 1: fetch OHLCV data
    hist = obb.equity.price.historical(
        symbol={repr(symbol)},
        start_date={repr(start_date)},
        provider="yfinance"
    )
    df = hist.to_dataframe().reset_index()

    # Step 2: run the technical indicator
    obj = obb
    for attr in {repr(path_parts)}:
        obj = getattr(obj, attr)

    res = obj(data=df, **{repr(indicator_kwargs)})

    if hasattr(res, "chart") and res.chart is not None:
        if hasattr(res.chart, "fig") and res.chart.fig is not None:
            html = res.chart.fig.to_html(include_plotlyjs="cdn", full_html=True,
                                          config={{"scrollZoom": True, "displayModeBar": True}})
            print(html)
        else:
            print("ERROR: Chart object has no figure.", file=sys.stderr)
            sys.exit(1)
    else:
        print("ERROR: No chart generated. Try a different indicator or symbol.", file=sys.stderr)
        sys.exit(1)
except Exception as e:
    print(f"ERROR: {{e}}", file=sys.stderr)
    sys.exit(1)
"""

        return f"""import sys
from openbb import obb

try:
    obj = obb
    for attr in {repr(path_parts)}:
        obj = getattr(obj, attr)

    res = obj(**{repr(kwargs)})

    if hasattr(res, "chart") and res.chart is not None:
        if hasattr(res.chart, "fig") and res.chart.fig is not None:
            html = res.chart.fig.to_html(include_plotlyjs="cdn", full_html=True, config={{"scrollZoom": True, "displayModeBar": True}})
            print(html)
        else:
            print("ERROR: Chart object has no figure.", file=sys.stderr)
            sys.exit(1)
    else:
        print("ERROR: No chart generated for this command.", file=sys.stderr)
        sys.exit(1)
except Exception as e:
    print(f"ERROR: {{e}}", file=sys.stderr)
    sys.exit(1)
"""

    def _build_onetime_script(self, path_parts: list, kwargs: dict) -> str:
        is_technical = path_parts[0] == "technical" if path_parts else False

        if is_technical:
            symbol = kwargs.get("symbol", "SPY")
            start_date = kwargs.get("start_date", "2023-01-01")
            indicator_kwargs = {k: v for k, v in kwargs.items()
                                if k not in ("symbol", "start_date", "end_date", "provider", "chart")}
            return f"""import sys, pandas as pd
from openbb import obb

try:
    hist = obb.equity.price.historical(symbol={repr(symbol)}, start_date={repr(start_date)}, provider="yfinance")
    df = hist.to_dataframe().reset_index()
    obj = obb
    for attr in {repr(path_parts)}:
        obj = getattr(obj, attr)
    res = obj(data=df, **{repr(indicator_kwargs)})
    if hasattr(res, "to_dataframe"):
        out = res.to_dataframe()
        if out.empty: print("Query returned no data.")
        else:
            print(out.head(25).to_string(index=False))
            if len(out) > 25: print(f"\\n... Showing 25 of {{len(out)}} rows")
    else:
        print(str(res))
except Exception as e:
    print(f"Error: {{e}}")
    sys.exit(1)
"""

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


async def get_chart_html(command_path: str, kwargs: dict) -> dict:
    """
    Execute an OpenBB command with chart=True and return the full Plotly HTML.
    Returns {"html": "...", "type": "chart_window"} or {"error": "...", "type": "error"}.
    """
    kwargs["chart"] = True
    return await openbb_native.execute(command_path, kwargs)

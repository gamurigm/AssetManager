import subprocess
import json
from pathlib import Path
from typing import Optional, Dict, Any, List
from app.core.logging import logger

class GSDService:
    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path(__file__).parent.parent.parent.parent
        self.gsd_bin = self.root_dir / ".gemini" / "get-shit-done" / "bin" / "gsd-tools.cjs"

    def _run_command(self, args: List[str]) -> Dict[str, Any]:
        """Run a gsd-tools.cjs command and return the JSON output."""
        cmd = ["node", str(self.gsd_bin)] + args + ["--raw"]
        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.root_dir),
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout.strip()
            try:
                return json.loads(output)
            except json.JSONDecodeError:
                return {"status": "success", "raw_output": output}
        except subprocess.CalledProcessError as e:
            logger.error(f"GSD Command Failed: {e.cmd} - {e.stderr}")
            return {"status": "error", "message": e.stderr.strip() or str(e)}
        except Exception as e:
            logger.error(f"GSD unexpected error: {e}")
            return {"status": "error", "message": str(e)}

    # State Operations
    def get_state(self, section: Optional[str] = None) -> Dict[str, Any]:
        args = ["state", "get"]
        if section:
            args.append(section)
        return self._run_command(args)

    def update_state(self, field: str, value: Any) -> Dict[str, Any]:
        return self._run_command(["state", "update", field, str(value)])

    def advance_plan(self) -> Dict[str, Any]:
        return self._run_command(["state", "advance-plan"])

    # Roadmap Operations
    def get_roadmap_analysis(self) -> Dict[str, Any]:
        return self._run_command(["roadmap", "analyze"])

    def add_phase(self, description: str) -> Dict[str, Any]:
        return self._run_command(["phase", "add", description])

    # Progress
    def get_progress(self, format: str = "json") -> Dict[str, Any]:
        return self._run_command(["progress", format])

    # Requirements
    def mark_requirement_complete(self, req_ids: List[str]) -> Dict[str, Any]:
        return self._run_command(["requirements", "mark-complete"] + req_ids)

    # Scaffolding
    def scaffold_plan(self, phase: str, plan: str, type: str = "execute") -> Dict[str, Any]:
        return self._run_command(["template", "fill", "plan", "--phase", phase, "--plan", plan, "--type", type])

    def scaffold_summary(self, phase: str, plan: str) -> Dict[str, Any]:
        return self._run_command(["template", "fill", "summary", "--phase", phase, "--plan", plan])

gsd_service = GSDService()

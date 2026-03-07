from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union
from datetime import datetime

class AgentMessage(BaseModel):
    role: str
    content: str
    agent_name: str
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Any]] = None

class TeamContext(BaseModel):
    chat_history: List[AgentMessage] = Field(default_factory=list)
    scratchpad: Dict[str, Any] = Field(default_factory=dict, description="Shared mutable state for key findings")
    task_queue: List[str] = Field(default_factory=list, description="Pending high-level tasks")
    completed_tasks: List[str] = Field(default_factory=list)

    # ── Hierarchical pipeline state ────────────────────────────────────────────
    # Analyst reports deposited by Quant / Macro / Fundamental / Risk analysts.
    # Keyed by agent name. ONLY Strategy Analyst may read and act on these.
    analyst_reports: Dict[str, str] = Field(
        default_factory=dict,
        description="Formal analysis reports submitted by each analyst tier agent",
    )
    # Risk report is stored separately so it is prominently accessible.
    risk_report: Optional[str] = Field(
        default=None,
        description="Formal risk assessment submitted by the Risk Manager",
    )
    # Signals that ONLY the Strategy Analyst can approve and deposit here.
    # The Trader may ONLY execute signals found in this list.
    approved_trade_signals: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Trade signals formally authorized by the Strategy Analyst",
    )

    # ── Convenience helpers ────────────────────────────────────────────────────
    def add_message(self, role: str, content: str, agent_name: str):
        self.chat_history.append(AgentMessage(role=role, content=content, agent_name=agent_name))

    def update_scratchpad(self, key: str, value: Any):
        self.scratchpad[key] = value

    def get_latest_message(self) -> Optional[AgentMessage]:
        return self.chat_history[-1] if self.chat_history else None

    # ── Report pipeline ────────────────────────────────────────────────────────
    def submit_report(self, agent_name: str, content: str) -> None:
        """Called by analyst-tier agents to formally submit their findings."""
        self.analyst_reports[agent_name] = content
        self.add_message("system", f"[REPORT SUBMITTED] {agent_name}", "System")

    def submit_risk_assessment(self, content: str) -> None:
        """Called by the Risk Manager to submit the session risk assessment."""
        self.risk_report = content
        self.add_message("system", "[RISK REPORT SUBMITTED] Risk Manager", "System")

    def get_all_reports(self) -> str:
        """Returns formatted text of all submitted analyst + risk reports."""
        parts: List[str] = []
        for agent_name, report in self.analyst_reports.items():
            parts.append(f"## {agent_name} REPORT\n{report}")
        if self.risk_report:
            parts.append(f"## RISK MANAGER REPORT\n{self.risk_report}")
        if not parts:
            return "No analyst or risk reports have been submitted yet."
        return "\n\n---\n\n".join(parts)

    # ── Signal pipeline ────────────────────────────────────────────────────────
    def approve_signal(self, signal: Dict[str, Any]) -> None:
        """Called exclusively by the Strategy Analyst to authorize a trade signal."""
        signal["authorized_at"] = datetime.now().isoformat()
        self.approved_trade_signals.append(signal)
        self.add_message(
            "system",
            f"[SIGNAL AUTHORIZED] {signal.get('symbol')} {signal.get('direction')} @ {signal.get('entry')}",
            "Strategy Analyst",
        )

    def get_approved_signals(self) -> List[Dict[str, Any]]:
        """Returns all signals authorized by the Strategy Analyst."""
        return list(self.approved_trade_signals)

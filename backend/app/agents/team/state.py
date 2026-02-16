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
    
    def add_message(self, role: str, content: str, agent_name: str):
        self.chat_history.append(AgentMessage(role=role, content=content, agent_name=agent_name))

    def update_scratchpad(self, key: str, value: Any):
        self.scratchpad[key] = value

    def get_latest_message(self) -> Optional[AgentMessage]:
        return self.chat_history[-1] if self.chat_history else None

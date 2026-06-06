from datetime import datetime
from pydantic import BaseModel


class AgentActivityEvent(BaseModel):
    agent_name: str
    action: str
    timestamp: datetime
    status: str
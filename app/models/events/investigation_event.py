from datetime import datetime

from pydantic import BaseModel


class InvestigationEvent(BaseModel):
    investigation_id: str
    incident_id: str
    agent_name: str
    action: str
    outcome: str
    timestamp: datetime
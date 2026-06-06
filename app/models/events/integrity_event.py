from datetime import datetime

from pydantic import BaseModel


class IntegrityEvent(BaseModel):
    incident_id: str
    risk_score: int
    status: str
    created_at: datetime
from pydantic import BaseModel
from datetime import datetime


class VoteEvent(BaseModel):
    event_id: str
    voter_id: str
    candidate: str
    timestamp: datetime
    device_id: str
    ip_address: str
    event_type: str = "vote_submitted"
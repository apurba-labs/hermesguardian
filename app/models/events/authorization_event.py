from pydantic import BaseModel
class AuthorizationEvent(BaseModel):
    authorization_id: str
    voter_id: str
    reason: str
    approved: bool
    validity_minutes: int
    approved_device: str
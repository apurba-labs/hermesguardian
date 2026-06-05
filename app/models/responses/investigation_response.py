from pydantic import BaseModel


class InvestigationResponse( BaseModel ):
    scenario: str
    status: str
    risk_score: int
    observations: list[str]
    recommendation: str
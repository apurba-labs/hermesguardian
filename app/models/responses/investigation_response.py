from pydantic import BaseModel
from typing import Dict, Any

class InvestigationResponse( BaseModel ):
    summary: str
    risk_score: int
    decision: str
    findings: list[str]
    integrity: Dict[str, Any]
    correlation: Dict[str, Any]
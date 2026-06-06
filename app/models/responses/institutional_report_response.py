from pydantic import BaseModel, Field
from typing import List
from typing import Dict, Any

class InvestigationResponse( BaseModel ):
    summary: str
    risk_score: int
    decision: str
    findings: list[str]
    integrity: Dict[str, Any]
    correlation: Dict[str, Any]
    
class InstitutionalReportResponse(BaseModel):
    summary: str = Field(description="The primary executive overview text.")
    risk_score: int = Field(description="Calculated operational risk integer from 0 to 100.")
    decision: str = Field(description="The formal governance state conclusion.")
    findings: List[str] = Field(description="List of specific isolated telemetry anomalies found.")
    recommendation: str = Field(description="Actionable operational steps for human reviewers.")
    confidence_level: str = Field(description="High, Medium, or Low with a brief justification.")
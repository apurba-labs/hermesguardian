from fastapi import APIRouter

from app.models.requests.investigation_request import (
    InvestigationRequest,
)

from app.models.responses.investigation_response import (
    InvestigationResponse,
)

from app.agents.supervisor_agent import (
    SupervisorAgent,
)

from app.services.scenario_loader import (
    load_scenario,
)

from app.services.integrity_analyzer import (
    analyze_vote,
)

router = APIRouter(prefix="/api")


@router.post( "/investigate", response_model=InvestigationResponse, )
def investigate( request: InvestigationRequest, ) -> InvestigationResponse:
    
    scenario = load_scenario(
        request.scenario
    )
    
    analysis = analyze_vote(scenario)
    
    supervisor = SupervisorAgent()
    
    report = supervisor.run(
        scenario,
        analysis
    )
    
    return InvestigationResponse(
        summary=report["summary"],
        risk_score=report["risk_score"],
        decision=report["decision"],
        findings=report["findings"],
        integrity=report["integrity"],      
        correlation=report["correlation"],
    )
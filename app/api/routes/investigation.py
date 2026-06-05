from fastapi import APIRouter

from app.models.requests.investigation_request import (
    InvestigationRequest,
)

from app.models.responses.investigation_response import (
    InvestigationResponse,
)

from app.services.scenario_loader import (
    load_scenario,
)

from app.services.integrity_analyzer import (
    analyze_vote,
)

router = APIRouter()


@router.post( "/investigate", response_model=InvestigationResponse, )
def investigate( request: InvestigationRequest, ) -> InvestigationResponse:
    
    scenario = load_scenario(
        request.scenario
    )

    analysis = analyze_vote(
        scenario
    )

    return InvestigationResponse(
        scenario=request.scenario,
        status=analysis["status"],
        risk_score=analysis["risk_score"],
        observations=analysis["observations"],
        recommendation=analysis["recommendation"],
    )
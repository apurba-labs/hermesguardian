from fastapi import APIRouter

from app.models.requests.investigation_request import (
    InvestigationRequest,
)

from app.models.responses.investigation_response import (
    InvestigationResponse,
)

router = APIRouter()


@router.post( "/investigate", response_model=InvestigationResponse, )
def investigate( request: InvestigationRequest, ) -> InvestigationResponse:

    return InvestigationResponse(
        status="success",
        scenario=request.scenario,
        message="Investigation started",
    )
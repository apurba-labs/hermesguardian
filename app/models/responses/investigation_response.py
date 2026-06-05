from pydantic import BaseModel


class InvestigationResponse( BaseModel ):
    status: str
    scenario: str
    message: str
from pydantic import BaseModel


class InvestigationRequest( BaseModel ):
    scenario: str
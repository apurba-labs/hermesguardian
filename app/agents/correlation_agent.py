from app.mcp.tools.vote_tools import (
    get_vote_events,
)

from app.mcp.tools.authorization_tools import (
    get_authorization_events,
)


class CorrelationAgent:

    def investigate(
        self,
        scenario,
    ):

        votes = get_vote_events()

        authorizations = (
            get_authorization_events()
        )

        return {
            "agent": "CorrelationAgent",
            "voter_id": scenario["voter_id"],
            "device_id": scenario["device_id"],
            "approved_device": scenario[
                "approved_device"
            ],
            "votes": [
                vote.model_dump()
                for vote in votes
            ],
            "authorizations": [
                auth.model_dump()
                for auth in authorizations
            ],
        }
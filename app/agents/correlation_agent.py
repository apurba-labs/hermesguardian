from app.mcp.tools.vote_tools import (
    get_vote_events,
)

from app.mcp.tools.authorization_tools import (
    get_authorization_events,
)


class CorrelationAgent:

    def investigate(self):

        return {
            "votes": get_vote_events(),
            "authorizations": get_authorization_events(),
        }
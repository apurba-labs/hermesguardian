from app.services.integrity_analyzer import (
    analyze_vote,
)


class IntegrityAgent:

    def investigate(
        self,
        scenario,
    ):

        return analyze_vote(
            scenario
        )
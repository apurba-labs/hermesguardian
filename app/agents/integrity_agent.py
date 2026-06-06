from app.mcp.tools.integrity_tools import (
    get_integrity_events,
)

class IntegrityAgent:

    def investigate(
        self,
        scenario,
        analysis,
    ):

        integrity_events = (
            get_integrity_events()
        )
        
        return {
            "agent": "IntegrityAgent",
            "status": analysis["status"],
            "risk_score": analysis["risk_score"],
            "observations": analysis[
                "observations"
            ],
            "integrity_events": [
                event.model_dump()
                for event in integrity_events
            ]
        }
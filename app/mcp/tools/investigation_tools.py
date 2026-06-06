from app.models.events import InvestigationEvent
from datetime import datetime


def get_investigation_events():
    return [
        InvestigationEvent(
            investigation_id="INV-001",
            incident_id="INC-001",
            agent_name="IntegrityAgent",
            action="Analyze Remote Vote",
            outcome="Low Risk",
            timestamp=datetime.utcnow()
        )
    ]
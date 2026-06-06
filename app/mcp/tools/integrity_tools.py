from datetime import datetime

from app.models.events import IntegrityEvent


def get_integrity_events():

    return [
        IntegrityEvent(
            incident_id="INC-001",
            risk_score=5,
            status="VERIFIED",
            created_at=datetime.utcnow(),
        )
    ]
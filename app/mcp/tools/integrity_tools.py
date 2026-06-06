"""
HermesGuardian MCP Integrity Tools

Current MVP implementation uses simulated integrity
events for investigation replay and dashboard visualization.

Future versions will retrieve integrity findings from
centralized observability and governance monitoring systems.
"""

from datetime import datetime

from app.models.events.integrity_event import (
    IntegrityEvent,
)


def get_integrity_events():

    return [
        IntegrityEvent(
            incident_id="INC-001",
            risk_score=5,
            status="VERIFIED",
            created_at=datetime.utcnow(),
        )
    ]
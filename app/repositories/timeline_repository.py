"""
HermesGuardian Timeline Repository

Current MVP implementation uses simulated investigation timelines
for dashboard visualization and workflow demonstrations.

Future versions will generate investigation timelines dynamically
from agent activity events and distributed telemetry traces.
"""
from datetime import datetime

from app.models.events.investigation_event import (
    InvestigationEvent,
)

def get_incident_timeline():

    return [
        InvestigationEvent(
            investigation_id="INV-001",
            incident_id="INC-001",
            agent_name="SupervisorAgent",
            action="Started investigation",
            outcome="COMPLETED",
            timestamp=datetime.utcnow(),
        ),
        InvestigationEvent(
            investigation_id="INV-001",
            incident_id="INC-001",
            agent_name="CorrelationAgent",
            action="Retrieved vote records",
            outcome="COMPLETED",
            timestamp=datetime.utcnow(),
        ),
        InvestigationEvent(
            investigation_id="INV-001",
            incident_id="INC-001",
            agent_name="IntegrityAgent",
            action="Calculated risk score",
            outcome="COMPLETED",
            timestamp=datetime.utcnow(),
        ),
        InvestigationEvent(
            investigation_id="INV-001",
            incident_id="INC-001",
            agent_name="ReportingAgent",
            action="Generated executive report",
            outcome="ACCEPTED",
            timestamp=datetime.utcnow(),
        ),
    ]


def save_timeline_event(event):
    """
    TODO:
    Persist timeline events to the investigation telemetry store.

    Future versions will reconstruct investigation timelines
    from agent activity and MCP event streams.
    """
    pass
"""
HermesGuardian Investigation Repository

Current MVP implementation uses simulated investigation
events for workflow replay and dashboard visualization.

Future versions will persist investigation traces and
agent execution telemetry through MCP and Dynatrace integrations.
"""

from datetime import datetime

from app.models.events.investigation_event import (
    InvestigationEvent,
)


def get_investigation_events():

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
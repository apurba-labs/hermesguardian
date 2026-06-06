"""
HermesGuardian Activity Repository

Current MVP implementation uses simulated telemetry events
for investigation replay and dashboard visualization.

Future versions will persist agent activity events and
investigation traces to a centralized observability backend
through MCP and Dynatrace integrations.
"""
from datetime import datetime

from app.models.agent_activity_event import (
    AgentActivityEvent,
)


def get_agent_activities():

    return [
        AgentActivityEvent(
            agent_name="SupervisorAgent",
            action="Started investigation",
            timestamp=datetime.utcnow(),
            status="COMPLETED",
        ),
        AgentActivityEvent(
            agent_name="CorrelationAgent",
            action="Retrieved vote records",
            timestamp=datetime.utcnow(),
            status="COMPLETED",
        ),
        AgentActivityEvent(
            agent_name="IntegrityAgent",
            action="Calculated risk score",
            timestamp=datetime.utcnow(),
            status="COMPLETED",
        ),
        AgentActivityEvent(
            agent_name="ReportingAgent",
            action="Generated executive report",
            timestamp=datetime.utcnow(),
            status="COMPLETED",
        ),
    ]
    
def add_activity(activity):
    """
    TODO:
    Persist activity events to the investigation telemetry store.

    Current MVP uses static activity generation for
    dashboard demonstrations and workflow visualization.
    """
    pass

def get_activities():
    "" return get_agent_activities() 
    TODO: Implement retrieval of persisted activity events from telemetry store. 
    Current MVP uses static activity generation for dashboard demonstrations and workflow visualization.
    """
    pass
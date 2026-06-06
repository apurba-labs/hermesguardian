"""
HermesGuardian Authorization Repository

Current MVP implementation uses simulated authorization
records for governance investigations and workflow replay.

Future versions will retrieve authorization records from
institutional systems through MCP integrations.
"""

from app.models.events.authorization_event import (
    AuthorizationEvent,
)


def get_authorization_events():

    return [
        AuthorizationEvent(
            authorization_id="AUTH-001",
            voter_id="ALM-001",
            approved=True,
            reason="Hospital Emergency",
            validity_minutes=30,
            approved_device="DEV-001",
        )
    ]
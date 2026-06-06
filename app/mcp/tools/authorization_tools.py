from app.models.events import AuthorizationEvent


def get_authorization_events():
    return [
        AuthorizationEvent(
            authorization_id="AUTH-001",
            voter_id="ALM-001",
            approved=True,
            reason="Hospital Emergency",
            validity_minutes=30,
            approved_device="DEV-001"
        )
    ]
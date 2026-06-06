from app.models.events import VoteEvent

def get_vote_events():
    return [
        VoteEvent(
            event_id="VT-001",
            voter_id="ALM-001",
            voter_batch="Batch-2018",
            candidate="Candidate-A",
            timestamp="2026-06-15T10:00:00",
            device_id="DEV-001",
            ip_address="103.120.45.10"
        )
    ]
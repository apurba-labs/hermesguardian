"""
HermesGuardian MCP Vote Tools

Current MVP implementation uses repository-backed
telemetry adapters.

Future versions will expose vote telemetry through
a dedicated MCP server implementation.
"""

from app.repositories.vote_repository import (
    get_vote_events,
)
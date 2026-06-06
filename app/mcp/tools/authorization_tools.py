"""
HermesGuardian MCP Authorization Tools

Current MVP implementation uses repository-backed
authorization telemetry adapters.

Future versions will expose authorization events
through a dedicated MCP server implementation.
"""

from app.repositories.authorization_repository import (
    get_authorization_events,
)
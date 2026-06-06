"""
HermesGuardian MCP Investigation Tools

Current MVP implementation uses repository-backed
investigation telemetry adapters.

Future versions will expose investigation traces
through a dedicated MCP server implementation.
"""

from app.repositories.investigation_repository import (
    get_investigation_events,
)
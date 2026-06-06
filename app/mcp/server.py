"""
HermesGuardian MCP Server

Current MVP uses local MCP-compatible tool adapters.

"""
from fastmcp import FastMCP

from app.mcp.tools.vote_tools import get_vote_events
from app.mcp.tools.authorization_tools import get_authorization_events
from app.mcp.tools.integrity_tools import get_integrity_events
from app.mcp.tools.investigation_tools import get_investigation_events

mcp = FastMCP("HermesGuardian")


@mcp.tool()
def get_votes():
    """Return voting telemetry events."""
    return [event.model_dump() for event in get_vote_events()]


@mcp.tool()
def get_authorizations():
    """Return authorization telemetry events."""
    return [event.model_dump() for event in get_authorization_events()]


@mcp.tool()
def get_integrity_incidents():
    """Return integrity incidents."""
    return [event.model_dump() for event in get_integrity_events()]


@mcp.tool()
def get_investigations():
    """Return investigation events."""
    return [event.model_dump() for event in get_investigation_events()]


if __name__ == "__main__":
    mcp.run()
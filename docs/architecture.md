# HermesGuardian Architecture

## Overview

HermesGuardian follows a layered architecture designed around governance investigations.

The platform separates user interaction, orchestration, agent reasoning, telemetry access, and reporting responsibilities.

## Architecture Flows

```text
               +--------------------------------------------------------+

               |                  STREAMLIT DASHBOARD                   |
               |                  (dashboard/app.py)                    |
               +---------------------------+----------------------------+

                                           |
                                           | HTTP POST /api/v1/investigation/run
                                           v
               +--------------------------------------------------------+

               |                FASTAPI INVESTIGATION API               |
               |            (app/api/routes/investigation.py)            |
               +---------------------------+----------------------------+

                                           |
                                           | Async Invoke / Instantiates
                                           v
               +--------------------------------------------------------+

               |                    SUPERVISOR AGENT                    |
               |             (app/agents/supervisor_agent.py)           |
               +-----+---------------------+----------------------+-----+

                     |                     |                      |
                     | Evaluates /         | Evaluates /          | Evaluates /
                     | Delegates           | Delegates            | Delegates
                     v                     v                      v
+--------------------------+ +--------------------------+ +--------------------------+

|    CORRELATION AGENT     | |     INTEGRITY AGENT      | |     REPORTING AGENT      |
| (app/agents/             | | (app/agents/             | | (app/agents/             |
|  correlation_agent.py)   | |  integrity_agent.py)     | |  reporting_agent.py)     |
+------------+-------------+ +------------+-------------+ +------------+-------------+

             |                            |                            |
             +----------------------------+----------------------------+

                                           |
                                           | Client tool_use via MCP (Stdio / SSE)
                                           v
               +--------------------------------------------------------+

               |                     FASTMCP SERVER                     |
               |                  (app/mcp/server.py)                   |
               +-----+---------------------+----------------------+-----+

                     |                     |                      |
                     | Exposes Tool        | Exposes Tool         | Exposes Tool
                     v                     v                      v
+--------------------------+ +--------------------------+ +--------------------------+

|        VOTE TOOL         | |    AUTHORIZATION TOOL    | |      INTEGRITY TOOL      |
| (app/mcp/tools/          | | (app/mcp/tools/          | | (app/mcp/tools/          |
|  vote_tools.py)          | |  authorization_tools.py) | |  integrity_tools.py)     |
+------------+-------------+ +------------+-------------+ +------------+-------------+

             |                            |                            |
             +----------------------------+----------------------------+

                                           |
                                           | Resolves via Repository Layer
                                           v
               +--------------------------------------------------------+

               |                 INSTITUTIONAL RECORDS                  |
               |                  (app/repositories/*)                  |
               +--------------------------------------------------------+
```


## Components

### Streamlit Dashboard

Provides:

* Voting Portal
* Investigation Submission
* Command Center
* Investigation Timeline
* Executive Reports

### FastAPI

Acts as the orchestration layer.

Responsibilities:

* Receive investigation requests
* Coordinate agent execution
* Return structured investigation results

### Supervisor Agent

Coordinates the investigation workflow and delegates responsibilities to specialized agents.

### Correlation Agent

Retrieves and correlates voting evidence through MCP tools.

### Integrity Agent

Evaluates governance policies and calculates integrity risk scores.

### Reporting Agent

Generates executive investigation reports and recommendations.

### FastMCP Server

Provides a standardized interface to institutional telemetry and governance records.

### Google Gemini

Provides AI-assisted reasoning and investigation analysis.

### Dynatrace Alignment

HermesGuardian treats governance workflows as observable systems.

* Vote Events → Telemetry Events
* Agent Activity → Traces
* Investigation Timeline → Distributed Trace
* Incidents → Observable Problems

This allows governance processes to benefit from observability principles traditionally used in software systems.

## Design Principles

* Transparency
* Explainability
* Auditability
* Human Oversight
* Institutional Trust

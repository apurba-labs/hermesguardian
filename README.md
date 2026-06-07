# HermesGuardian

HermesGuardian is an AI-powered Governance Integrity Intelligence Platform that combines Google Gemini 2.5 Flash, Multi-Agent Investigations, MCP-powered telemetry, and Dynatrace observability to investigate exceptional governance events and generate transparent, auditable institutional decisions.

---

## Architecture Overview

HermesGuardian follows a modular multi-agent architecture designed to separate evidence collection, integrity analysis, AI reasoning, and observability.

```text
Voting Portal (Streamlit)
           │
           ▼
    FastAPI Backend
           │
           ▼
     SupervisorAgent
      ├─────────────┐
      ▼             ▼
CorrelationAgent  IntegrityAgent
      │             │
      └──────┬──────┘
             ▼
      ReportingAgent
             │
             ▼
  Google Gemini 2.5 Flash
             │
             ▼
 Executive Governance Report
             │
     ┌───────┴────────┐
     ▼                ▼
MCP Telemetry     Dynatrace
    Server       Observability
```

---

## Core Components

### SupervisorAgent

Coordinates the investigation lifecycle and orchestrates specialized agents.

Responsibilities:

* Investigation workflow management
* Agent coordination
* Result aggregation

### CorrelationAgent

Collects governance telemetry and correlates investigation evidence.

Responsibilities:

* Vote telemetry collection
* Authorization evidence retrieval
* Investigation trace correlation

### IntegrityAgent

Performs deterministic integrity analysis.

Responsibilities:

* Policy validation
* Risk score calculation
* Governance rule evaluation

### ReportingAgent

Generates executive governance assessments.

Responsibilities:

* Report generation
* Google Gemini integration
* Governance summary creation

---

## Investigation Workflow

1. Governance event submitted through the Voting Portal
2. FastAPI API receives investigation request
3. Scenario configuration is loaded
4. SupervisorAgent orchestrates investigation
5. CorrelationAgent gathers telemetry
6. IntegrityAgent evaluates compliance and risk
7. ReportingAgent invokes Google Gemini 2.5 Flash
8. Executive report is generated
9. Investigation data is exposed through MCP
10. Observability events are published to Dynatrace

---

## Supported Investigation Scenarios

### Authorized Remote Vote

Expected Outcome:

* Risk Score: Low
* Decision: Accepted

### Device Mismatch Vote

Expected Outcome:

* Risk Score: Elevated
* Decision: Manual Review

### Expired Authorization Vote

Expected Outcome:

* Risk Score: Critical
* Decision: Rejected

---

## Google Gemini Integration

HermesGuardian uses Google Gemini 2.5 Flash to generate executive governance assessments.

Design Principles:

* Deterministic systems calculate risk scores
* AI generates governance narratives
* AI does not determine investigation outcomes
* Human oversight remains central

This separation ensures explainability and auditability.

---

## MCP Telemetry Server

HermesGuardian exposes governance telemetry through FastMCP.

Available MCP Tools:

```python
get_votes()

get_authorizations()

get_integrity_incidents()

get_investigations()
```

The MCP layer enables AI agents and external systems to access governance evidence through a standardized interface.

---

## Dynatrace Integration

HermesGuardian transforms governance investigations into observable business events.

Published Event Categories:

* Governance Business Events
* Investigation Traces
* Integrity Incidents
* Risk Indicators
* Agent Workflow Metadata

Example Event Payload:

```json
{
  "title": "HermesGuardian Institutional Governance Audit",
  "eventType": "CUSTOM_INFO",
  "properties": {
    "business_event": "Remote Vote Submission",
    "problem_status": "ACCEPTED",
    "risk_score": "0",
    "voter_id": "ALM-2026-991"
  }
}
```

---

## Technology Stack

### Backend

* FastAPI
* Python 3.12
* Pydantic
* Uvicorn

### AI

* Google Gemini 2.5 Flash
* Google GenAI SDK

### Observability

* Dynatrace Events API
* Governance Event Mapping

### Agent Infrastructure

* FastMCP
* Multi-Agent Architecture

### Frontend

* Streamlit

---

## Running HermesGuardian

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

### Start Dashboard

```bash
streamlit run dashboard/app.py
```

### Start MCP Server

```bash
python -m app.mcp.server
```

---

## Project Structure

```text
app/
├── agents/
├── api/
├── mcp/
├── models/
├── repositories/
├── services/
├── scenarios/

dashboard/
├── components/
├── pages/

tests/
```

---

## Future Roadmap

* Real-time governance monitoring
* Historical investigation analytics
* OpenTelemetry support
* Expanded Dynatrace observability
* Additional governance workflows
* Enterprise compliance reporting

---

## License

MIT License

# HermesGuardian

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-orange)
![Dynatrace](https://img.shields.io/badge/Dynatrace-Observability-brightgreen)
![MCP](https://img.shields.io/badge/FastMCP-Telemetry-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

HermesGuardian is an AI-powered Governance Integrity Intelligence Platform that combines Google Gemini 2.5 Flash, Multi-Agent Investigations, MCP-powered telemetry, and Dynatrace observability to investigate exceptional governance events and generate transparent, auditable institutional decisions.

[![Live Demo](https://img.shields.io/badge/Live-Demo-success)](https://hermesguardian.gotihub.com)

🚀 Built for the Google Cloud Rapid Agent Hackathon 2026

---

## Overview

Institutions occasionally face exceptional governance situations where standard procedures must be temporarily bypassed. Emergency remote voting, device verification failures, and authorization exceptions can introduce uncertainty, reduce transparency, and make post-event investigations difficult.

HermesGuardian helps institutions investigate these events through evidence correlation, deterministic risk analysis, AI-assisted reasoning, and observability-driven governance workflows.

---

## Architecture Overview

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

This separation ensures explainability, transparency, and auditability.

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
    "voter_id": "ALM-2026-991",
    "agent_workflow": "SupervisorAgent -> ReportingAgent",
    "confidence_level": "High (Gemini 2.5 Flash Verified)"
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

## Prerequisites

* Python 3.12+
* Google Gemini API Key
* Dynatrace Tenant (Optional)
* Git

HermesGuardian has been tested using Python 3.12 and Google Gemini 2.5 Flash.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/apurba-labs/hermesguardian.git

cd hermesguardian
```

### Create Virtual Environment

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
GEMINI_API_KEY=your_google_gemini_api_key

DYNATRACE_BASE_URL=https://your-tenant.live.dynatrace.com

DYNATRACE_API_TOKEN=your_dynatrace_api_token
```

---

## Running HermesGuardian

### Start FastAPI Backend

```bash
uvicorn app.api.main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

### Start Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

### Start MCP Server

```bash
python -m app.mcp.server
```
## Deployment

HermesGuardian is containerized using Docker and deployed behind a shared Nginx reverse proxy infrastructure.

Production deployment includes:

FastAPI Backend Service
Streamlit Governance Dashboard
Google Gemini 2.5 Flash Integration
FastMCP Telemetry Server
Dynatrace Event Ingestion Pipeline
Docker Compose Orchestration
Shared Nginx Reverse Proxy with SSL Termination

Live Environment:

https://hermesguardian.gotihub.com

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

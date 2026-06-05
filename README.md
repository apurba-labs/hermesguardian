# HermesGuardian

HermesGuardian is an AI-powered governance integrity platform designed to investigate exceptional voting events and help institutions make transparent, evidence-based decisions.

Built for the Google Cloud Rapid Agent Hackathon, HermesGuardian combines Google Gemini, FastAPI, FastMCP, and Dynatrace observability concepts to evaluate governance workflows and generate executive investigation reports.

## Problem

Traditional voting systems record votes.

They rarely investigate votes.

Organizations frequently face exceptional situations such as:

* Hospital emergency voting
* Overseas voters
* Device verification requirements
* Expired voting authorizations

These situations require policy validation, evidence collection, and transparent decision making.

HermesGuardian helps institutions investigate these events through AI-powered agent workflows.

## Key Features

* Multi-agent investigation workflow
* Google Gemini reasoning
* FastAPI orchestration layer
* FastMCP-powered institutional telemetry
* Governance integrity analysis
* Executive investigation reports
* Observability-driven investigation timeline
* Interactive command center dashboard

## Architecture

Voting Event

↓

FastAPI Investigation API

↓

Supervisor Agent

├── Correlation Agent

├── Integrity Agent

└── Reporting Agent

↓

FastMCP Tools

├── Vote Events

├── Authorization Events

└── Integrity Events

↓

Executive Investigation Report

## Investigation Scenarios

HermesGuardian currently supports:

1. Authorized Remote Vote
2. Device Mismatch Vote
3. Expired Authorization Vote

Each scenario produces a unique investigation outcome and recommendation.

## Technology Stack

* Python
* FastAPI
* Streamlit
* Google Gemini
* FastMCP
* Pydantic
* Dynatrace Observability Concepts

## Potential Applications

* Alumni Association Elections
* University Governance
* NGO Voting
* Professional Associations
* Cooperative Societies
* Community Boards

## Vision

Our vision is to combine AI reasoning, institutional telemetry, and observability principles to improve trust, transparency, and accountability in governance processes.

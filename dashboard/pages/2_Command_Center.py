import sys
from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Component layouts
from dashboard.components.metrics import render_metrics
from dashboard.components.incident_card import render_incident
from dashboard.components.timeline import render_timeline

st.title("🛡️ HermesGuardian Command Center")
st.write("Multi-Agent Institutional Integrity Intelligence Control Plane")
st.markdown("---")

report = st.session_state.get("report")
selected_scenario = st.session_state.get("selected_scenario", "none")

# --------------------------------------------------
# 1. Overview & Dynamic Metrics Simulation
# --------------------------------------------------
if report:
    decision_val = report.get("decision", "UNKNOWN")
    if decision_val == "ACCEPTED":
        st.sidebar.metric("System Risk Level", "LOW RISK", "0/100")
    elif decision_val == "MANUAL REVIEW":
        st.sidebar.metric("System Risk Level", "ELEVATED RISK", "50/100", delta_color="inverse")
    else:
        st.sidebar.metric("System Risk Level", "CRITICAL RISK", f"{report.get('risk_score', 100)}/100", delta_color="inverse")

render_metrics()

# --------------------------------------------------
# 2. Executive Investigation Report
# --------------------------------------------------
if report:
    st.subheader("📋 Executive Investigation Report")
    
    current_decision = report.get("decision", "PENDING")
    summary_text = report.get("summary", "")
    
    if current_decision == "ACCEPTED":
        st.success(f"**VERDICT: {current_decision}** \n\n {summary_text}")
    elif current_decision == "MANUAL REVIEW":
        st.warning(f"**VERDICT: {current_decision}** \n\n {summary_text}")
    else:
        st.error(f"**VERDICT: {current_decision}** \n\n {summary_text}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Calculated Risk Score", value=f"{report.get('risk_score', 0)}/100")
    with col2:
        st.metric(label="Compliance Decision", value=current_decision)

    st.subheader("🔍 Key Findings")
    # Gracefully match either findings list or fallback observations matrix
    findings_list = report.get("findings") if report.get("findings") else report.get("integrity", {}).get("observations", [])
    for finding in findings_list:
        st.markdown(f"• {finding}")

    # --------------------------------------------------
    # 3. Evidence Explorer (Live Mapping Integration)
    # --------------------------------------------------
    st.subheader("🔬 Multi-Agent Evidence & Traces")
    
    with st.expander("🤖 Agent Reasoning Traces"):
        st.json({
            "IntegrityAgent_Analysis": report.get("integrity"),
            "CorrelationAgent_Analysis": report.get("correlation")
        })

    with st.expander("📡 Connected MCP Investigation Evidence"):
        correlation_data = report.get("correlation", {})
        integrity_data = report.get("integrity", {})

        st.markdown("#### Vote Event Telemetry")
        if "votes" in correlation_data:
            st.write(correlation_data["votes"])
        else:
            st.info("No vote event telemetry found in this scenario response.")
        
        st.markdown("#### Authorization Event Logs")
        if "authorizations" in correlation_data:
            st.write(correlation_data["authorizations"])
        else:
            st.info("No authorization trace logs found in this scenario response.")
    
        st.markdown("#### Security Cluster Fault Events")
        if "integrity_events" in integrity_data:
            st.write(integrity_data["integrity_events"])
        else:
            st.info("No security cluster fault events recorded.")

    with st.expander("🔭 Dynatrace Live Observability Gateway"):
        sync_status = report.get("observability_sync", "UNKNOWN")
        
        if sync_status == "SUCCESS":
            st.success("✅ **Grail Pipeline State: Stream Synced Live**")
        else:
            st.info("ℹ️ **Grail Pipeline State: Simulation Mode / Local Only**")
            
        st.markdown("#### Outbound Event Ingest Parameters")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Event Pipeline Routing Type", "CUSTOM_INFO")
            st.metric("Source Engine Identity", "HermesGuardian Platform")
        with col2:
            st.metric("Target Cluster Gateway", "Tenant wkf10640")
            st.metric("API Endpoint Binding", "/api/v2/events/ingest")

        st.markdown("#### Transmitted Properties Matrix")
        st.code(f"""
{{
    "title": "HermesGuardian Institutional Governance Audit",
    "eventType": "CUSTOM_INFO",
    "properties": {{
        "business_event": "Remote Vote Submission",
        "problem_status": "{current_decision}",
        "risk_score": "{report.get('risk_score', 0)}",
        "voter_id": "{correlation_data.get('voter_id', 'N/A')}",
        "agent_workflow": "SupervisorAgent -> ReportingAgent",
        "confidence_level": "High (Gemini 2.5 Flash Verified)"
    }}
}}
        """, language="json")

    with st.expander("📦 Raw JSON Payload (Full Report)"):
        st.json(report)

else:
    st.warning("⚠️ No active investigation trace found in memory. Please submit a vote from the Voting Portal page first.")

# --------------------------------------------------
# 4. Governance Context
# --------------------------------------------------
st.markdown("---")
st.subheader("⚖️ Institutional Governance Reference")
voter_ctx = st.session_state.get("voter_context", {"voter_id": "N/A", "batch": "N/A", "reason": "Hospital Emergency"})

st.info(f"""
* **Target Institution:** Alumni Association Election Committee
* **Evaluated Identity:** User ID `{voter_ctx['voter_id']}` ({voter_ctx['batch']})
* **Exempt Policy Rule:** Emergency Remote Authorization Exception
* **Exempt Reason Parameter:** {voter_ctx['reason']}
* **Security Constraints:** Hardware Pinning Verification Required | Token TTL < 30m
""")
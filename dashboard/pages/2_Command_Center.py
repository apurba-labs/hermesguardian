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
# We inject dynamic values into our metrics based on the active threat scenario
if report:
    if report.get("decision") == "ACCEPTED":
        st.sidebar.metric("System Risk Level", "LOW RISK", "0/100")
    elif report.get("decision") == "MANUAL REVIEW":
        st.sidebar.metric("System Risk Level", "ELEVATED RISK", "50/100", delta_color="inverse")
    else:
        st.sidebar.metric("System Risk Level", "CRITICAL RISK", f"{report.get('risk_score')}/100", delta_color="inverse")

render_metrics()

# --------------------------------------------------
# 2. Executive Investigation Report
# --------------------------------------------------
if report:
    st.subheader("📋 Executive Investigation Report")
    
    if report["decision"] == "ACCEPTED":
        st.success(f"**VERDICT: {report['decision']}** — {report['summary']}")
    elif report["decision"] == "MANUAL REVIEW":
        st.warning(f"**VERDICT: {report['decision']}** — {report['summary']}")
    else:
        st.error(f"**VERDICT: {report['decision']}** — {report['summary']}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Calculated Risk Score", value=f"{report.get('risk_score')}/100")
    with col2:
        st.metric(label="Compliance Decision", value=report.get("decision", "PENDING"))

    st.subheader("🔍 Key Findings")
    for finding in report.get("findings", []):
        st.markdown(f"• {finding}")

    # --------------------------------------------------
    # 3. Evidence Explorer (Fixed & Formatted)
    # --------------------------------------------------
    st.subheader("🔬 Multi-Agent Evidence & Traces")
    
    with st.expander("🤖 Agent Reasoning Traces"):
        # Display how our sub-agents analyzed the scenario data
        st.json({
            "IntegrityAgent_Analysis": report.get("integrity"),
            "CorrelationAgent_Analysis": report.get("correlation")
        })

    with st.expander("📡 Connected MCP Investigation Evidence"):
        # Using .get() prevents KeyError crashes if the keys are missing
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
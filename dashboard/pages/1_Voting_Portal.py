import sys
from pathlib import Path
import requests
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import settings

st.title("🗳️ HermesGuardian Voting Portal")

st.markdown("""
Submit a vote for the Alumni Committee Election.
Remote voting requires authorization.
""")

voter_id = st.text_input("Voter ID", value="ALM-2026-991")
batch = st.text_input("Batch", value="Batch-2018")
candidate = st.selectbox("Candidate", ["Candidate-A", "Candidate-B"])
remote_vote = st.checkbox("Emergency Remote Vote", value=True)

reason = ""
if remote_vote:
    reason = st.selectbox(
        "Reason",
        ["Hospital Emergency", "Overseas Travel", "Disability Assistance"]
    )

scenario_option = st.selectbox(
    "Investigation Scenario",
    ["Authorized Remote Vote", "Device Mismatch", "Expired Authorization"]
)

SCENARIO_MAP = {
    "Authorized Remote Vote": "authorized_remote_vote",
    "Device Mismatch": "device_mismatch_vote",
    "Expired Authorization": "expired_authorization_vote",
}

if st.button("Submit Vote", type="primary"):
    selected_scenario = SCENARIO_MAP[scenario_option]

    try:
        response = requests.post(
            f"{settings.API_BASE_URL}/investigate",
            json={"scenario": selected_scenario},
            timeout=30,
        )
        response.raise_for_status()
        report = response.json()

        # Save everything to state session scope for dynamic component sharing
        st.session_state["report"] = report
        st.session_state["selected_scenario"] = selected_scenario
        st.session_state["voter_context"] = {
            "voter_id": voter_id,
            "batch": batch,
            "reason": reason
        }

        st.success(f"Investigation completed for: {scenario_option}!")
        st.info("👈 Navigate to the Command Center to inspect the live agent breakdown.")

    except Exception as exc:
        st.error(f"Investigation failed: {exc}")

st.markdown("---")
st.info("""
### Emergency Voting Policy
✓ Committee approval required  
✓ One-time voting token required  
✓ Device verification required  
✓ Limited voting window  
✓ Full audit trail generated  
✓ AI-assisted integrity review
""")
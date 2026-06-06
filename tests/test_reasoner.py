import sys
from pathlib import Path

# Initialize path boundaries cleanly
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.services.gemini_reasoner import generate_integrity_report

def run_reasoner_test():
    print("🤖 Initializing HermesGuardian Gemini Reasoner Test Probe...")

    # Mock Scenario matching Scenario 2 (Device Mismatch Trigger)
    mock_scenario = {
        "voter_id": "ALM-2026-991",
        "batch": "Batch-2018",
        "candidate": "Candidate-A",
        "timestamp": "2026-06-01T02:14:00",
        "device_id": "DEV-7777",  # Unregistered hardware footprint
        "ip_address": "103.120.45.10"
    }

    # Mock Agent Triage Metrics
    mock_analysis = {
        "status": "REVIEW",
        "risk_score": 50,
        "observations": [
            "Remote voting authorized due to Hospital Emergency.",
            "CRITICAL EXCEPTION: Active session device_id (DEV-7777) deviated from pre-approved identity pinning schema baseline.",
            "Token validity timeline within nominal parameters (30m window)."
        ]
    }

    print("📤 Sending prompt matrices and tool schemas to Gemini 2.5 Flash...")
    report_output = generate_integrity_report(mock_scenario, mock_analysis)

    if report_output:
        print("\n🎉 ==================================================")
        print("✅ SUCCESS: Gemini Inference Cycle Completed Successfully!")
        print("==================================================\n")
        print(report_output)
    else:
        print("\n❌ FAILURE: Gemini inference engine returned empty response or threw an exception.")

if __name__ == "__main__":
    run_reasoner_test()
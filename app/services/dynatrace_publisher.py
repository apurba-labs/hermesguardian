import os
import requests
from app.core.config import settings

class DynatracePublisher:
    def __init__(self):
        self.environment_url = settings.DT_ENVIRONMENT.rstrip("/")
        self.personal_token = settings.DT_PERSONAL_ACCESS_TOKEN

    def send_governance_event(self, report: dict) -> bool:
        """
        Pushes multi-agent governance findings straight to Dynatrace Events v2 Ingest API 
        using your verified Personal Access Token.
        """
        if not self.personal_token or not self.environment_url:
            print("Skipping Dynatrace Ingestion: Missing token or environment URL configurations.")
            return False

        ingest_url = f"{self.environment_url}/api/v2/events/ingest"
        
        event_payload = {
            "eventType": "CUSTOM_INFO",
            "title": "HermesGuardian Institutional Governance Audit",
            "source": "HermesGuardian Platform Engine",
            "entitySelector": "type(SERVICE)",
            "properties": {
                "business_event": "Remote Vote Submission",
                "problem_status": str(report.get("decision", "UNKNOWN")),
                "risk_score": str(report.get("risk_score", 0)),
                "voter_id": str(report.get("correlation", {}).get("voter_id", "N/A")),
                "agent_workflow": "SupervisorAgent -> ReportingAgent",
                "confidence_level": "High (Gemini 2.5 Flash Verified)"
            }
        }

        headers = {
            "Authorization": f"Api-Token {self.personal_token}",
            "Content-Type": "application/json; charset=utf-8"
        }

        try:
            response = requests.post(ingest_url, json=event_payload, headers=headers, timeout=10)
            if response.status_code in [200, 201, 202]:
                print("✅ Telemetry successfully pushed to Dynatrace via Personal Access Token!")
                return True
            else:
                print(f"⚠️ Dynatrace Ingestion Warning: Status {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Network failure during Dynatrace transmission: {str(e)}")
            return False

dt_publisher = DynatracePublisher()
import sys
import os
from pathlib import Path
import requests

# 1. Initialize path bindings exactly like your Gemini test script
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# Load our core settings profile
from app.core.config import settings

def test_dynatrace_handshake():
    print("📡 Initializing HermesGuardian Dynatrace Test Probe...")
    
    # Extract the configuration keys out of your active runtime environment settings
    # Ensure DT_ENVIRONMENT and DT_PERSONAL_ACCESS_TOKEN are populated in your .env or shell memory
    env_url = os.getenv("DT_ENVIRONMENT", settings.DT_ENVIRONMENT).rstrip("/")
    pat_token = os.getenv("DT_PERSONAL_ACCESS_TOKEN", getattr(settings, "DT_PERSONAL_ACCESS_TOKEN", ""))

    if not env_url or not pat_token:
        print("❌ Error: Missing configuration. Ensure DT_ENVIRONMENT and DT_PERSONAL_ACCESS_TOKEN are set!")
        return

    print(f"🔗 Target Endpoint: {env_url}/api/v2/events")
    
    # 2. Build out a lightweight verification payload structure matching Dynatrace Events v2
    test_payload = {
        "eventType": "CUSTOM_INFO",
        "title": "HermesGuardian Verification Ping",
        "source": "Manual Engineering Test Script",
        "entitySelector": "type(SERVICE)",
        "properties": {
            "integration_status": "PENDING_VERIFICATION",
            "test_message": "Say HermesGuardian Dynatrace integration successful."
        }
    }

    # 3. Apply standard token authorization formatting requirements
    headers = {
        "Authorization": f"Api-Token {pat_token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    try:
        print("📤 Transmitting telemetry payload packet over HTTP POST...")
        response = requests.post(f"{env_url}/api/v2/events/ingest", json=test_payload, headers=headers, timeout=10)
        print(f"📥 Received Response Status Code: {response.status_code}")
        
        # Dynatrace Event API returns 201 Created or 200 OK on successful ingestion
        if response.status_code in [200, 201, 202]:
            print("\n🎉 ==================================================")
            print("✅ SUCCESS: HermesGuardian Dynatrace integration successful!")
            print("==================================================\n")
            print(f"Response Payload Details:\n{response.text}")
        else:
            print("\n⚠️ ==================================================")
            print("❌ FAILURE: Ingestion rejected by Dynatrace Gateway Architecture.")
            print("==================================================")
            print(f"Status Code: {response.status_code}")
            print(f"Error Details: {response.text}\n")
            print("👉 Check if your token has the 'events.ingest' scope active under your profile settings.")

    except Exception as e:
        print("\n💥 ==================================================")
        print("❌ CRITICAL EXCEPTION: Local network thread failed to route packet.")
        print("==================================================")
        print(f"System Error: {str(e)}\n")

if __name__ == "__main__":
    test_dynatrace_handshake()
import json
from datetime import datetime
from google import genai
from app.core.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate_integrity_report(
    scenario,
    analysis,
):

    prompt = f"""
You are HermesGuardian.

HermesGuardian is a Multi-Agent Governance Integrity Platform.

Analyze the provided governance telemetry and integrity findings.

Rules:

- Never accuse individuals of fraud.
- Never provide legal conclusions.
- Focus on operational anomalies.
- Use professional governance language.
- Recommend institutional review when appropriate.

Scenario:
{json.dumps(scenario, indent=2, default=lambda o: o.isoformat() if isinstance(o, datetime) else str(o))}

Integrity Analysis:
{json.dumps(analysis, indent=2, default=lambda o: o.isoformat() if isinstance(o, datetime) else str(o))}

Generate:

1. Executive Summary
2. Integrity Assessment
3. Key Observations
4. Risk Evaluation
5. Recommendation
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception:

        return None
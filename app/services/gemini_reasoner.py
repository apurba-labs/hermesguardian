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

HermesGuardian is an AI-powered Governance Integrity Platform.

Scenario:
{json.dumps(scenario, indent=2, default=str)}

Integrity Decision:
Status: {analysis["status"]}
Risk Score: {analysis["risk_score"]}

Observations:
{chr(10).join([f"- {o}" for o in analysis["observations"]])}

Instructions:

- Explain the investigation outcome.
- Focus on governance and compliance.
- Do not accuse individuals of wrongdoing.
- Do not provide legal conclusions.
- Use professional institutional language.
- Keep the report concise and executive-friendly.

Generate:

1. Executive Summary
2. Integrity Assessment
3. Key Observations
4. Recommendation
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception:

        return None
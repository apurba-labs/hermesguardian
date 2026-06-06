import json
from datetime import datetime
from google import genai
from app.core.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def generate_integrity_report(
    scenario: dict,
    analysis: dict,
) -> str:
    """
    Generates a structured executive integrity assessment using Gemini 2.5 Flash.
    """
    # 1. Capture current date context for precise timeline evaluation rules
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Build the structured engineering prompt
    prompt = f"""
You are HermesGuardian, an advanced AI-powered Governance Integrity Platform.
Your purpose is to synthesize technical telemetry and forensic anomalies into high-level executive insights.

[CONTEXT ENGINE]
- Evaluation Runtime Horizon: 2026-06-06 (Current System Time: {current_time_str})

[TARGET TELEMETRY DATA]
Scenario Footprint:
{json.dumps(scenario, indent=2, default=str)}

Deterministic Triage Core Parameters:
- Status: {analysis.get("status", "UNKNOWN")}
- Risk Score: {analysis.get("risk_score", 0)}

Operational Checklist Observations:
{chr(10).join([f"- {o}" for o in analysis.get("observations", [])])}

[STRICT COMPLIANCE DIRECTIVES]
- Grounding Rule: Rely strictly on the provided dataset. Do not assume, extrapolate, or hallucinate historical variables.
- Operational Focus: Center all arguments on governance deviations, device profile matches, network boundaries, and compliance.
- Tone Control: Always use professional, balanced, corporate institutional terminology.
- Legal Boundary: Never accuse individuals or organizations of malicious fraud or intent. Do not deliver definitive legal rulings.
- Formatting: Keep the assessment clear, action-oriented, and immediately executive-friendly.

[EXPECTED OUTPUT FORMAT]
Generate exactly the following numbered markdown sections:
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

    except Exception as e:
        print(f"❌ Gemini Inference Thread Exception: {str(e)}")
        return None
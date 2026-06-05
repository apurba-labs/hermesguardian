def generate_investigation_summary(
    scenario,
    analysis,
):

    summary = f"""
Investigation Summary
=====================

Election: {scenario['event']}
Voter ID: {scenario['voter_id']}

Integrity Status: {analysis['status']}
Risk Score: {analysis['risk_score']}/100

Observations:
"""

    for item in analysis["observations"]:
        summary += f"\n- {item}"

    summary += f"""

Recommendation:
{analysis['recommendation']}
"""

    return summary
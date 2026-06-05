def generate_report(
    scenario,
    analysis,
):

    return {
        "event": scenario["event"],
        "voter_id": scenario["voter_id"],
        "status": analysis["status"],
        "risk_score": analysis["risk_score"],
        "observations": analysis["observations"],
        "recommendation": analysis["recommendation"],
    }
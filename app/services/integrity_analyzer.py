def analyze_vote(data):

    observations = []
    risk_score = 0

    # Authorization Check
    if data["remote_voting_authorized"]:
        observations.append(
            "Authorized remote voting"
        )
    else:
        observations.append(
            "Unauthorized remote voting"
        )
        risk_score += 50

    # Device Verification
    if data["device_id"] == data["approved_device"]:
        observations.append(
            "Device matched"
        )
    else:
        observations.append(
            "Device mismatch"
        )
        risk_score += 30

    # Authorization Window Validation
    elapsed = data.get(
        "elapsed_minutes",
        0
    )

    validity = data.get(
        "validity_minutes",
        30
    )

    if elapsed > validity:

        observations.append(
            "Authorization expired"
        )

        risk_score += 80

    else:

        observations.append(
            "Authorization valid"
        )

    # Risk Classification
    if risk_score < 20:

        status = "VERIFIED"

    elif risk_score < 80:

        status = "REVIEW"

    else:

        status = "REJECTED"

    # Recommendation
    if status == "VERIFIED":

        recommendation = (
            "Accept vote"
        )

    elif status == "REVIEW":

        recommendation = (
            "Institutional review required"
        )

    else:

        recommendation = (
            "Reject vote"
        )

    return {
        "status": status,
        "risk_score": risk_score,
        "observations": observations,
        "recommendation": recommendation,
    }
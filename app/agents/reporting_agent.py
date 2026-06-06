class ReportingAgent:

    def generate(
        self,
        integrity_result,
        correlation_result,
    ):

        risk_score = integrity_result["risk_score"]

        status = integrity_result["status"]

        observations = integrity_result[
            "observations"
        ]

        if status == "VERIFIED":

            summary = (
                "Authorized remote vote verified."
            )

            decision = "ACCEPTED"

        elif status == "REVIEW":

            summary = (
                "Potential integrity concerns detected."
            )

            decision = "MANUAL REVIEW"

        else:

            summary = (
                "Integrity violation detected."
            )

            decision = "REJECTED"

        return {
            "agent": "ReportingAgent",
            "summary": summary,
            "risk_score": risk_score,
            "decision": decision,
            "findings": observations,
            "integrity": integrity_result,
            "correlation": correlation_result,
        }
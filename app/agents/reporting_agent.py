from app.services.gemini_reasoner import (
    generate_integrity_report,
)

from app.services.dynatrace_mapper import (
    build_observability_snapshot,
)


class ReportingAgent:

    def generate(
        self,
        scenario,
        integrity_result,
        correlation_result,
    ):

        risk_score = integrity_result["risk_score"]

        status = integrity_result["status"]

        observations = integrity_result[
            "observations"
        ]

        if status == "VERIFIED":

            fallback_summary = (
                "Authorized remote vote verified."
            )

            decision = "ACCEPTED"

        elif status == "REVIEW":

            fallback_summary = (
                "Potential integrity concerns detected."
            )

            decision = "MANUAL REVIEW"

        else:

            fallback_summary = (
                "Integrity violation detected."
            )

            decision = "REJECTED"
        
        
        gemini_analysis = {
            "status": integrity_result["status"],
            "risk_score": integrity_result["risk_score"],
            "observations": integrity_result["observations"],
        }
        
        ai_summary = (
            generate_integrity_report(
                scenario,
                gemini_analysis,
            )
        )
        
        summary = (
            ai_summary
            if ai_summary
            else fallback_summary
        )

        report_payload = {
            "agent": "ReportingAgent",
            "summary": summary,
            "risk_score": risk_score,
            "decision": decision,
            "findings": observations,
            "integrity": integrity_result,
            "correlation": correlation_result,
        }
        
        report_payload["observability"] = (
            build_observability_snapshot(
                report_payload
            )
        )

        return report_payload
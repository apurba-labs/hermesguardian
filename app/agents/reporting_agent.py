from app.services.report_generator import (
    generate_report,
)


class ReportingAgent:

    def generate(
        self,
        scenario,
        analysis,
        correlation_result,
    ):

        report = generate_report(
            scenario,
            analysis,
        )

        status = analysis["status"]

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

        report["summary"] = summary
        report["decision"] = decision
        report["findings"] = analysis[
            "observations"
        ]

        report["integrity"] = analysis

        report["correlation"] = (
            correlation_result
        )

        return report
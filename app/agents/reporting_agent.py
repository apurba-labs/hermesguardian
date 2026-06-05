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

        report["evidence"] = (
            correlation_result
        )

        return report
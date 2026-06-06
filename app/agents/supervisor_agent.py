from app.agents.integrity_agent import IntegrityAgent
from app.agents.correlation_agent import CorrelationAgent
from app.agents.reporting_agent import ReportingAgent


class SupervisorAgent:

    def run(
        self,
        scenario,
        analysis,
    ):

        integrity_agent = IntegrityAgent()

        correlation_agent = CorrelationAgent()

        reporting_agent = ReportingAgent()

        integrity_result = (
            integrity_agent.investigate(
                scenario,
                analysis,
            )
        )

        correlation_result = (
            correlation_agent.investigate(
                scenario,
            )
        )

        report = reporting_agent.generate(
            integrity_result,
            correlation_result,
        )

        return report
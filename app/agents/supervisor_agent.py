from app.agents.correlation_agent import (
    CorrelationAgent,
)

from app.agents.integrity_agent import (
    IntegrityAgent,
)

from app.agents.reporting_agent import (
    ReportingAgent,
)


class SupervisorAgent:

    def run(
        self,
        scenario,
    ):

        correlation_agent = (
            CorrelationAgent()
        )

        integrity_agent = (
            IntegrityAgent()
        )

        reporting_agent = (
            ReportingAgent()
        )

        correlation_result = (
            correlation_agent.investigate()
        )

        analysis = (
            integrity_agent.investigate(
                scenario
            )
        )

        report = (
            reporting_agent.generate(
                scenario,
                analysis,
                correlation_result,
            )
        )

        return report
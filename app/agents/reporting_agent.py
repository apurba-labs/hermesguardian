from app.services.gemini_reasoner import generate_integrity_report
from app.services.dynatrace_publisher import dt_publisher

class ReportingAgent:

    def generate(
        self,
        scenario: dict,
        integrity_result: dict,
        correlation_result: dict,
    ) -> dict:

        status = integrity_result.get("status")
        observations = integrity_result.get("observations", [])

        # 1. Base Fallback Configurations
        if status == "VERIFIED":
            fallback_summary = "Authorized remote vote verified."
            fallback_decision = "ACCEPTED"
            fallback_risk = integrity_result.get("risk_score", 0)
        elif status == "REVIEW":
            fallback_summary = "Potential integrity concerns detected."
            fallback_decision = "MANUAL REVIEW"
            fallback_risk = integrity_result.get("risk_score", 40)
        else:
            fallback_summary = "Integrity violation detected."
            fallback_decision = "REJECTED"
            fallback_risk = integrity_result.get("risk_score", 80)
        
        gemini_analysis = {
            "status": status,
            "risk_score": integrity_result.get("risk_score", 0),
            "observations": observations,
            "recommendation": integrity_result.get("recommendation", "Execute human-in-the-loop validation review.")
        }
        
        # 2. Invoke Gemini 2.5 Flash Structured Inference Brain
        try:
            ai_report_schema = generate_integrity_report(scenario, gemini_analysis)
            
            # Extract values out of the guaranteed Pydantic schema object
            summary = ai_report_schema.summary
            risk_score = ai_report_schema.risk_score
            decision = ai_report_schema.decision
            findings = ai_report_schema.findings
            
        except Exception:
            # Fallback values if the entire block degrades
            summary = fallback_summary
            decision = fallback_decision
            risk_score = fallback_risk
            findings = observations

        # 3. Construct the Unified Report Payload Contract
        report_payload = {
            "agent": "ReportingAgent",
            "summary": summary,
            "risk_score": risk_score,
            "decision": decision,
            "findings": findings,
            "integrity": integrity_result,
            "correlation": correlation_result,
        }
        
        # 4. LIVE INGESTION: Fire the data straight into Dynatrace Grail Data Lakehouse
        # This will securely run using the OAuth clients scopes!
        try:
            dt_publisher.send_governance_event(report_payload)
            report_payload["observability_sync"] = "SUCCESS"
        except Exception as dt_err:
            print(f"⚠️ Dynatrace sync deferred: {str(dt_err)}")
            report_payload["observability_sync"] = "DEFERRED"

        return report_payload
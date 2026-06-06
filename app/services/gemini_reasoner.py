import json
import sys
import os
import asyncio
from datetime import datetime
from pathlib import Path
from google import genai
from google.genai import types
from app.core.config import settings

# Import official MCP primitives and Server Parameters class object
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Initialize the official Google GenAI Client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

# Dynamically resolve absolute paths to prevent production directory context issues
BASE_DIR = Path(__file__).resolve().parents[2]
SERVER_SCRIPT_PATH = str(BASE_DIR / "app" / "mcp" / "server.py")

def clean_gemini_schema(schema: dict) -> dict:
    """
    Recursively strips out 'additionalProperties' and 'additional_properties'
    to comply with strict Google GenAI SDK function declaration guidelines.
    """
    if not isinstance(schema, dict):
        return schema
    
    cleaned = {k: clean_gemini_schema(v) for k, v in schema.items() 
               if k not in ["additionalProperties", "additional_properties"]}
    return cleaned

async def generate_integrity_report_async(scenario: dict, analysis: dict) -> str:
    """
    Asynchronously links to the FastMCP server, discovers its live tools catalog,
    and dynamically orchestrates a multi-turn agentic tool execution loop with Gemini.
    """
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append project root to the background thread's environment pathing matrix
    env_config = os.environ.copy()
    env_config["PYTHONPATH"] = str(BASE_DIR)

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[SERVER_SCRIPT_PATH],
        env=env_config
    )

    # Establish the communication channel with the background FastMCP process
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Complete the protocol handshake execution
            await session.initialize()
            
            # Pull the live exposed tool specifications dynamically from server.py
            mcp_tools_list = await session.list_tools()
            
            # Map discovered tools into structural definitions compliant with Google GenAI SDK
            gemini_tools = []
            for tool in mcp_tools_list.tools:
                raw_schema = tool.input_schema if hasattr(tool, 'input_schema') else tool.inputSchema
                # Clean the parameters schema to satisfy Gemini's strict payload formatting rules
                cleaned_schema = clean_gemini_schema(dict(raw_schema)) if raw_schema else {"type": "object", "properties": {}}
                
                gemini_tools.append({
                    "function_declarations": [{
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": cleaned_schema
                    }]
                })

            # Formulate the executive analysis guidelines prompt
            prompt = f"""
You are HermesGuardian, an advanced AI-powered Governance Integrity Platform.
Your purpose is to synthesize technical telemetry and forensic anomalies into high-level executive insights.

[CONTEXT ENGINE]
- Evaluation Runtime Horizon: 2026-06-06 (Current System Time: {current_time_str})

[TARGET TELEMETRY DATA]
Scenario Footprint:
{json.dumps(scenario, indent=2, default=str)}

Deterministic Triage Core Parameters:
- Status: {analysis.get("status", "UNKNOWN")}
- Risk Score: {analysis.get("risk_score", 0)}

Operational Checklist Observations:
{chr(10).join([f"- {o}" for o in analysis.get("observations", [])])}

[STRICT COMPLIANCE DIRECTIVES]
- Grounding Rule: Rely strictly on the provided dataset. Do not assume, extrapolate, or hallucinate historical variables.
- Operational Focus: Center all arguments on governance deviations, device profile matches, network boundaries, and compliance.
- Tone Control: Always use professional, balanced, corporate institutional terminology.
- Legal Boundary: Never accuse individuals or organizations of malicious fraud or intent. Do not deliver definitive legal rulings.
- Formatting: Keep the assessment clear, action-oriented, and immediately executive-friendly.

[EXPECTED OUTPUT FORMAT]
Generate exactly the following numbered markdown sections:
1. Executive Summary
2. Integrity Assessment
3. Key Observations
4. Recommendation
"""

            try:
                # 1. Start a dynamic multi-turn chat session with Gemini to support tool execution history
                chat = client.chats.create(model="gemini-2.5-flash")
                
                # First inference pass containing the dynamic live tool schemas over the wire
                config = types.GenerateContentConfig(tools=gemini_tools, temperature=0.2)
                response = chat.send_message(prompt, config=config)
                
                # 2. Enter the Agentic Loop: Check if Gemini requested any tool calls
                while response.function_calls:
                    tool_responses = []
                    
                    for call in response.function_calls:
                        print(f"🤖 Gemini Agent triggered MCP tool call request: {call.name} with args: {call.args}")
                        
                        tool_args = dict(call.args) if call.args else {}
                        mcp_result = await session.call_tool(call.name, arguments=tool_args)
                        result_content = "".join([chunk.text for chunk in mcp_result.content if hasattr(chunk, 'text')])
                        
                        tool_responses.append(
                            types.Part.from_function_response(
                                name=call.name,
                                response={"result": result_content}
                            )
                        )
                    
                    response = chat.send_message(tool_responses, config=config)

                return response.text

            except Exception as e:
                print(f"❌ Core Gemini tool-inference cycle failure: {str(e)}")
                return None

def generate_integrity_report(scenario: dict, analysis: dict) -> str:
    """
    Synchronous lifecycle entrypoint wrapper to support your current 
    Supervisor and Agent processing architectures without breaks.
    """
    return asyncio.run(generate_integrity_report_async(scenario, analysis))
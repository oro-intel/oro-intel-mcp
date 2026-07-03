"""LlamaIndex agent with live UK procurement data via the Oro Intel remote MCP server.

Usage: ORO_API_KEY=oro_... ANTHROPIC_API_KEY=sk-ant-... python agent.py
Requires: pip install llama-index llama-index-tools-mcp llama-index-llms-anthropic
"""

import asyncio
import os

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.anthropic import Anthropic
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

ORO_API_KEY = os.environ["ORO_API_KEY"]  # https://app.oro-intel.com/dashboard/developers

mcp_client = BasicMCPClient(
    "https://api.oro-intel.com/mcp/",  # trailing slash required
    headers={"Authorization": f"Bearer {ORO_API_KEY}"},
)


async def main() -> None:
    tools = await McpToolSpec(client=mcp_client).to_tool_list_async()
    agent = FunctionAgent(
        tools=tools,
        llm=Anthropic(model="claude-sonnet-5"),
        system_prompt="You answer questions about UK public procurement using the oro_* tools.",
    )
    response = await agent.run(
        "Look up the UK company 'Serco' and give me its full supplier profile. "
        "Report how many public contracts it has won, and the credits_charged "
        "and credits_remaining from the tool responses."
    )
    print(response)


asyncio.run(main())

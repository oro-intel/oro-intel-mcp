"""LangChain agent with live UK procurement data via the Oro Intel remote MCP server.

Usage: ORO_API_KEY=oro_... ANTHROPIC_API_KEY=sk-ant-... python agent.py
Requires: pip install langchain-mcp-adapters langgraph "langchain[anthropic]"
"""

import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

ORO_API_KEY = os.environ["ORO_API_KEY"]  # https://app.oro-intel.com/dashboard/developers

client = MultiServerMCPClient(
    {
        "oro-intel": {
            "transport": "streamable_http",
            "url": "https://api.oro-intel.com/mcp/",  # trailing slash required
            "headers": {"Authorization": f"Bearer {ORO_API_KEY}"},
        }
    }
)


async def main() -> None:
    tools = await client.get_tools()
    agent = create_react_agent("anthropic:claude-sonnet-5", tools)
    result = await agent.ainvoke(
        {
            "messages": [
                (
                    "user",
                    "Look up the UK company 'Serco' and give me its full supplier "
                    "profile. Report how many public contracts it has won, and the "
                    "credits_charged and credits_remaining from the tool responses.",
                )
            ]
        }
    )
    print(result["messages"][-1].content)


asyncio.run(main())

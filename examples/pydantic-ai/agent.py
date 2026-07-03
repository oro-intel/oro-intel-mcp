"""PydanticAI agent with live UK procurement data via the Oro Intel remote MCP server.

Usage: ORO_API_KEY=oro_... ANTHROPIC_API_KEY=sk-ant-... python agent.py
Requires: pip install "pydantic-ai-slim[mcp,anthropic]"
"""

import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

ORO_API_KEY = os.environ["ORO_API_KEY"]  # https://app.oro-intel.com/dashboard/developers

server = MCPServerStreamableHTTP(
    url="https://api.oro-intel.com/mcp/",  # trailing slash required
    headers={"Authorization": f"Bearer {ORO_API_KEY}"},
)

agent = Agent("anthropic:claude-sonnet-5", toolsets=[server])


async def main() -> None:
    async with agent:
        result = await agent.run(
            "Look up the UK company 'Serco' and give me its full supplier profile. "
            "Report how many public contracts it has won, and the credits_charged "
            "and credits_remaining from the tool responses."
        )
    print(result.output)


asyncio.run(main())

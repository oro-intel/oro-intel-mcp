// Vercel AI SDK agent with live UK procurement data via the Oro Intel remote MCP server.
// Usage: ORO_API_KEY=oro_... ANTHROPIC_API_KEY=sk-ant-... node agent.mjs
// Requires: npm install ai @ai-sdk/anthropic @modelcontextprotocol/sdk

import { anthropic } from "@ai-sdk/anthropic";
import { experimental_createMCPClient, generateText, stepCountIs } from "ai";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const ORO_API_KEY = process.env.ORO_API_KEY; // https://app.oro-intel.com/dashboard/developers
if (!ORO_API_KEY) throw new Error("Set ORO_API_KEY");

const mcpClient = await experimental_createMCPClient({
  transport: new StreamableHTTPClientTransport(
    new URL("https://api.oro-intel.com/mcp/"), // trailing slash required
    { requestInit: { headers: { Authorization: `Bearer ${ORO_API_KEY}` } } },
  ),
});

try {
  const tools = await mcpClient.tools();
  const { text } = await generateText({
    model: anthropic("claude-sonnet-5"),
    tools,
    stopWhen: stepCountIs(6),
    prompt:
      "Look up the UK company 'Serco' and give me its full supplier profile. " +
      "Report how many public contracts it has won, and the credits_charged " +
      "and credits_remaining from the tool responses.",
  });
  console.log(text);
} finally {
  await mcpClient.close();
}

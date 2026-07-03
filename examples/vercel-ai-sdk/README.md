# Vercel AI SDK

A `generateText` agent using Oro Intel's tools over the **remote MCP server** (`experimental_createMCPClient` + streamable-HTTP transport) to resolve a company and fetch its full profile, reporting credits used.
Run: `npm install ai @ai-sdk/anthropic @modelcontextprotocol/sdk` then `ORO_API_KEY=oro_... ANTHROPIC_API_KEY=... node agent.mjs`.

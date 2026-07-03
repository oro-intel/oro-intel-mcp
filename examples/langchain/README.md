# LangChain

A LangGraph ReAct agent using Oro Intel's tools over the **remote MCP server** (via `langchain-mcp-adapters`) to resolve a company and fetch its full profile, reporting credits used.
Run: `pip install langchain-mcp-adapters langgraph "langchain[anthropic]"` then `ORO_API_KEY=oro_... ANTHROPIC_API_KEY=... python agent.py`.

# OpenAI function calling

Exposes two Oro Intel **REST** endpoints as OpenAI function tools (lookup company → full profile) and lets the model drive the flow, printing credits per call.
Run: `pip install openai httpx` then `ORO_API_KEY=oro_... OPENAI_API_KEY=... python agent.py` (REST — OpenAI Chat Completions has no remote-MCP client here).

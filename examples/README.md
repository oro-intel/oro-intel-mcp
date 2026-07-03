# Examples

Every example runs the flagship flow — resolve a UK company by name, then fetch
its full supplier profile — and prints `credits_charged` / `credits_remaining`.
All read the key from the `ORO_API_KEY` env var
(create one at <https://app.oro-intel.com/dashboard/developers>; 250 free credits
on signup). The full flow costs 17 credits (5 lookup + 12 profile).

| Folder | Stack | Transport |
|---|---|---|
| [`curl/`](./curl) | bash + curl | REST |
| [`python/`](./python) | Python, httpx | REST |
| [`javascript/`](./javascript) | Node 18+, fetch | REST |
| [`langchain/`](./langchain) | LangChain / LangGraph | remote MCP |
| [`llamaindex/`](./llamaindex) | LlamaIndex | remote MCP |
| [`openai-function-calling/`](./openai-function-calling) | OpenAI SDK | REST |
| [`vercel-ai-sdk/`](./vercel-ai-sdk) | Vercel AI SDK | remote MCP |
| [`pydantic-ai/`](./pydantic-ai) | PydanticAI | remote MCP |

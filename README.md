# Oro Intel MCP — UK Public Procurement Data for AI Agents

[![MCP](https://img.shields.io/badge/MCP-streamable--http-blue)](https://documentation.oro-intel.com/docs/mcp)
[![Docs](https://img.shields.io/badge/docs-oro--intel-black)](https://documentation.oro-intel.com)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1-green)](https://api.oro-intel.com/openapi.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

UK public procurement data for AI agents — tenders, contracts, buyer and supplier
profiles over MCP and REST. 250 free credits.

Give any AI agent live UK public-sector procurement data — tender notices, awarded
contracts, buyer (council/department) and supplier profiles — over MCP or a plain
REST API. Same account, same credits, both transports. Charged on success only.

- **What it covers:** UK Contracts Finder + Find a Tender notices, awarded
  contracts and their documents, company/supplier profiles, buyer profiles,
  frameworks, bulk export.
- **Who it's for:** agent builders, procurement/bid-writing tools,
  market-intelligence and govtech apps.
- **Remote & hosted:** nothing to run locally. Point your client at the URL.
- **Auth:** sign in with OAuth (interactive clients — no key to copy), or send an
  API key as `Authorization: Bearer oro_...` (headless agents and scripts).

## 60-second quickstart

1. Interactive client (Claude, ChatGPT, Cursor…): add the server below and **sign
   in when prompted** — done. Headless/scripts: create a key at
   <https://app.oro-intel.com/dashboard/developers> (shown once).
2. Add the server to your client (matrix below).
3. Ask: *"search UK tenders for EV charging in the last 30 days."*

## Install

> Endpoint: `https://api.oro-intel.com/mcp/` — **keep the trailing slash**.
> Interactive clients: OAuth sign-in, no header needed.
> Headless: header `Authorization: Bearer oro_YOUR_KEY`.

<details open><summary><b>Claude Code</b></summary>

```bash
claude mcp add --transport http oro-intel https://api.oro-intel.com/mcp/
```

Sign in in the browser window that opens (or run `/mcp` → **oro-intel →
Authenticate**). For headless use, pass a key instead:

```bash
claude mcp add --transport http oro-intel https://api.oro-intel.com/mcp/ \
  --header "Authorization: Bearer oro_YOUR_KEY"
```

If the header is dropped, add to `~/.claude.json` under `mcpServers`:

```json
"oro-intel": {
  "type": "http",
  "url": "https://api.oro-intel.com/mcp/",
  "headers": { "Authorization": "Bearer oro_YOUR_KEY" }
}
```
</details>

<details><summary><b>Claude Desktop &amp; claude.ai</b></summary>

**Settings → Connectors → Add custom connector.** Name it `Oro Intel`, paste
`https://api.oro-intel.com/mcp/`, click **Add**, sign in when prompted.

Or edit `claude_desktop_config.json`:

```json
{ "mcpServers": { "oro-intel": {
  "type": "http",
  "url": "https://api.oro-intel.com/mcp/",
  "headers": { "Authorization": "Bearer oro_YOUR_KEY" } } } }
```
</details>

<details><summary><b>Cursor</b></summary>

**Settings → MCP → Add new MCP server**, or `.cursor/mcp.json`
(project) / `~/.cursor/mcp.json` (global):

```json
{ "mcpServers": { "oro-intel": {
  "url": "https://api.oro-intel.com/mcp/",
  "headers": { "Authorization": "Bearer oro_YOUR_KEY" } } } }
```

Omit `headers` to use OAuth sign-in instead.
</details>

<details><summary><b>Windsurf</b></summary>

`~/.codeium/windsurf/mcp_config.json`:

```json
{ "mcpServers": { "oro-intel": {
  "serverUrl": "https://api.oro-intel.com/mcp/",
  "headers": { "Authorization": "Bearer oro_YOUR_KEY" } } } }
```
</details>

<details><summary><b>VS Code (Copilot agent mode)</b></summary>

`.vscode/mcp.json`:

```json
{ "servers": { "oro-intel": {
    "type": "http",
    "url": "https://api.oro-intel.com/mcp/",
    "headers": { "Authorization": "Bearer ${input:oro_key}" } } },
  "inputs": [ { "type": "promptString", "id": "oro_key",
    "description": "Oro Intel API key", "password": true } ] }
```
</details>

<details><summary><b>ChatGPT (Developer Mode)</b></summary>

**Settings → Apps & Connectors → Advanced settings → Developer mode** (Plus/Pro),
then **Create connector** with MCP server URL `https://api.oro-intel.com/mcp/`.
Choose OAuth and sign in when prompted. (Remote streamable-HTTP only.)
</details>

<details><summary><b>Codex</b></summary>

```bash
codex mcp add oro-intel --url https://api.oro-intel.com/mcp/
```

Or `~/.codex/config.toml`:

```toml
[mcp_servers.oro-intel]
url = "https://api.oro-intel.com/mcp/"
```
</details>

<details><summary><b>Gemini CLI</b></summary>

`~/.gemini/settings.json`:

```json
{ "mcpServers": { "oro-intel": { "httpUrl": "https://api.oro-intel.com/mcp/" } } }
```

Restart the CLI and sign in in the browser window that opens on first use.
</details>

<details><summary><b>Cline / any other client</b></summary>

Any client that supports remote streamable-HTTP MCP works: URL
`https://api.oro-intel.com/mcp/`, and either OAuth sign-in or the header
`Authorization: Bearer oro_YOUR_KEY`.

```json
"oro-intel": {
  "type": "http",
  "url": "https://api.oro-intel.com/mcp/",
  "headers": { "Authorization": "Bearer oro_YOUR_KEY" }
}
```
</details>

## Tools

The MCP tools mirror the [REST API](https://documentation.oro-intel.com/docs/api)
one-to-one and carry the same credit costs. Each tool description states its cost,
so the agent knows before it calls. 1 credit = £0.01.

| Tool | What it returns | Credits |
|---|---|---|
| `oro_search_notices` | Search tender/contract notices | 2 |
| `oro_search_tenders` | Search live (open) tenders | 2 |
| `oro_lookup_contract` | Full record for one notice/contract | 5 |
| `oro_contract_documents` | Documents attached to a contract | 10 |
| `oro_lookup_company` | Resolve a company name → record | 5 |
| `oro_company_contracts` | Contracts a company has won | 10 |
| `oro_company_profile` | **Flagship** — full supplier profile: core record + every contract won, one call | 12 |
| `oro_lookup_buyer` | Resolve a buyer (council/dept) name → record | 5 |
| `oro_buyer_contracts` | Contracts a buyer has issued | 10 |
| `oro_buyer_profile` | Full buyer profile | 20 |
| `oro_lookup_framework` | Framework agreement record | 5 |
| `oro_bulk_export` | Bulk pull for a query | 100 / 1,000 rows |
| `oro_get_balance` | Remaining credits | free |

## Auth & credits

One account covers both API and MCP. **250 free credits on signup**; 1 credit =
£0.01. Charged on **success only** — an empty lookup isn't billed. Pass an
`Idempotency-Key` header so retries never double-bill. Out of credits →
`402 insufficient_credits` with a `top_up_url` in the body.

Every metered response echoes `credits_charged` and `credits_remaining`.

## Also available as a REST API

Prefer plain HTTP? Same data, same key: `https://api.oro-intel.com/v1/*`
(OpenAPI 3.1: <https://api.oro-intel.com/openapi.json>).

```bash
curl -s "https://api.oro-intel.com/v1/companies/search?name=Serco" \
  -H "Authorization: Bearer $ORO_API_KEY"
```

## Examples

Runnable snippets in [`/examples`](./examples): curl · Python · JavaScript ·
LangChain · LlamaIndex · OpenAI function calling · Vercel AI SDK · PydanticAI.
Every example runs the flagship flow — resolve a company by name, then fetch its
full profile — and prints `credits_charged` / `credits_remaining`.

## Links

Docs <https://documentation.oro-intel.com> ·
MCP guide <https://documentation.oro-intel.com/docs/mcp> ·
Quickstart <https://documentation.oro-intel.com/docs/quickstart> ·
Agents start here <https://documentation.oro-intel.com/llms.txt> ·
Status <https://documentation.oro-intel.com/docs/status> ·
Changelog [CHANGELOG.md](./CHANGELOG.md)

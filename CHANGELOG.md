# Changelog

All notable changes to the Oro Intel MCP server and API are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-07-03

### Added

- Remote streamable-HTTP MCP server at `https://api.oro-intel.com/mcp/`
  (OAuth sign-in or `Authorization: Bearer oro_...`).
- 13 tools, mirroring the REST API one-to-one: `oro_search_notices`,
  `oro_search_tenders`, `oro_lookup_contract`, `oro_contract_documents`,
  `oro_lookup_company`, `oro_company_contracts`, `oro_company_profile`
  (flagship), `oro_lookup_buyer`, `oro_buyer_contracts`, `oro_buyer_profile`,
  `oro_lookup_framework`, `oro_bulk_export`, `oro_get_balance`.
- REST API v1 at `https://api.oro-intel.com/v1/*` with OpenAPI 3.1 spec at
  `https://api.oro-intel.com/openapi.json`.
- Credit metering: 1 credit = £0.01, 250 free on signup, charged on success
  only, `Idempotency-Key` support, `402 insufficient_credits` with `top_up_url`.

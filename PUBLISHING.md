# Publishing to the official MCP registry

The manifest is [`server.json`](./server.json) (schema `2025-12-11`, remote
streamable-HTTP server — no package to build).

## Manual publish

```bash
# install the publisher CLI (see github.com/modelcontextprotocol/registry for
# current install options; brew/binary releases available)
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).tar.gz" | tar xz mcp-publisher

# authenticate for the io.github.oro-intel namespace — sign in as a member of
# the oro-intel GitHub org
./mcp-publisher login github

# validate + publish from the repo root
./mcp-publisher publish
```

Verify: `curl "https://registry.modelcontextprotocol.io/v0/servers?search=oro-intel"`.

## CI publish (on tag)

`.github/workflows/publish-registry.yml` publishes on any `v*` tag using GitHub
OIDC (no secrets needed — OIDC proves the repo belongs to the `oro-intel` org,
which grants the `io.github.oro-intel/*` namespace).

Release flow: bump `version` in `server.json` → update `CHANGELOG.md` →
`git tag v1.x.y && git push --tags`.

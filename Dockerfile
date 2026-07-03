# Thin stdio wrapper for the hosted Oro Intel MCP server, for platforms
# (e.g. Glama inspection) that start servers from a Dockerfile. The real
# server is remote at https://api.oro-intel.com/mcp/ — this just proxies
# stdio <-> streamable HTTP via mcp-remote.
#
# Interactive auth: mcp-remote opens an OAuth flow. Headless: pass a key with
#   docker run -e ORO_API_KEY=oro_... <image>
FROM node:22-alpine

RUN npm install -g mcp-remote

# --header uses ORO_API_KEY when provided; without it mcp-remote falls back
# to the server's OAuth flow.
ENTRYPOINT ["sh", "-c", "exec mcp-remote https://api.oro-intel.com/mcp/ ${ORO_API_KEY:+--header \"Authorization: Bearer ${ORO_API_KEY}\"}"]

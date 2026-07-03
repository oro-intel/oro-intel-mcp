#!/usr/bin/env bash
# Resolve a company by name, then fetch its full profile (the flagship call).
# Usage: ORO_API_KEY=oro_... ./company-profile.sh "Serco"
set -euo pipefail
: "${ORO_API_KEY:?Set ORO_API_KEY (create one at https://app.oro-intel.com/dashboard/developers)}"
QUERY="${1:-Serco}"
BASE="https://api.oro-intel.com/v1"
AUTH="Authorization: Bearer $ORO_API_KEY"

# 1. Resolve name -> company_number (5 credits)
SEARCH=$(curl -sf "$BASE/companies/search?name=$(printf %s "$QUERY" | sed 's/ /%20/g')" -H "$AUTH")
NUMBER=$(printf %s "$SEARCH" | python -c "import json,sys; d=json.load(sys.stdin); n=d['companies_house_number']; sys.exit(f'Best match {d[\"name\"]!r} has no Companies House number') if not n else print(n)")
echo "Resolved '$QUERY' -> company_number $NUMBER (credits_charged=$(printf %s "$SEARCH" | python -c "import json,sys; print(json.load(sys.stdin)['credits_charged'])"))"

# 2. Full profile: core record + every contract won, one call (12 credits)
curl -sf "$BASE/companies/$NUMBER/profile" -H "$AUTH" \
  | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('core',{}),indent=2)[:600]); print('contracts:', d.get('contracts',{}).get('contract_count')); print('credits_charged:', d['credits_charged']); print('credits_remaining:', d['credits_remaining'])"

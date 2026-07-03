"""Resolve a UK company by name, then fetch its full profile (flagship call).

Usage: ORO_API_KEY=oro_... python company_profile.py "Serco"
Requires: pip install httpx
"""

import os
import sys

import httpx

API_KEY = os.environ["ORO_API_KEY"]  # https://app.oro-intel.com/dashboard/developers
BASE = "https://api.oro-intel.com/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

query = sys.argv[1] if len(sys.argv) > 1 else "Serco"

with httpx.Client(base_url=BASE, headers=HEADERS, timeout=30) as client:
    # 1. Resolve name -> company_number (5 credits)
    # Returns the single best match: core record incl. companies_house_number
    search = client.get("/companies/search", params={"name": query}).raise_for_status().json()
    number = search["companies_house_number"]
    if not number:
        sys.exit(f"Best match {search['name']!r} has no Companies House number — try a more specific name.")
    print(f"Resolved {query!r} -> {number} (credits_charged={search['credits_charged']})")

    # 2. Full profile: core record + every contract won, one call (12 credits)
    profile = client.get(f"/companies/{number}/profile").raise_for_status().json()
    print("name:", profile["core"].get("name"))
    print("contracts won:", profile["contracts"]["contract_count"])
    print("credits_charged:", profile["credits_charged"])
    print("credits_remaining:", profile["credits_remaining"])

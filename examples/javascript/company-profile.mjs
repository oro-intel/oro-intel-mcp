// Resolve a UK company by name, then fetch its full profile (flagship call).
// Usage: ORO_API_KEY=oro_... node company-profile.mjs "Serco"
// Requires Node 18+ (built-in fetch). No dependencies.

const API_KEY = process.env.ORO_API_KEY; // https://app.oro-intel.com/dashboard/developers
if (!API_KEY) throw new Error("Set ORO_API_KEY");
const BASE = "https://api.oro-intel.com/v1";
const headers = { Authorization: `Bearer ${API_KEY}` };
const query = process.argv[2] ?? "Serco";

async function get(path) {
  const res = await fetch(`${BASE}${path}`, { headers });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  return res.json();
}

// 1. Resolve name -> company_number (5 credits)
const search = await get(`/companies/search?name=${encodeURIComponent(query)}`);
const number = search.items[0].company_number;
console.log(`Resolved "${query}" -> ${number} (credits_charged=${search.credits_charged})`);

// 2. Full profile: core record + every contract won, one call (12 credits)
const profile = await get(`/companies/${number}/profile`);
console.log("name:", profile.core?.name);
console.log("contracts won:", profile.contracts?.contract_count);
console.log("credits_charged:", profile.credits_charged);
console.log("credits_remaining:", profile.credits_remaining);

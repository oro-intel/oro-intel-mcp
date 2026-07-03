"""OpenAI function calling against the Oro Intel REST API (no MCP client needed).

Usage: ORO_API_KEY=oro_... OPENAI_API_KEY=sk-... python agent.py
Requires: pip install openai httpx
"""

import json
import os

import httpx
from openai import OpenAI

ORO_API_KEY = os.environ["ORO_API_KEY"]  # https://app.oro-intel.com/dashboard/developers
oro = httpx.Client(
    base_url="https://api.oro-intel.com/v1",
    headers={"Authorization": f"Bearer {ORO_API_KEY}"},
    timeout=30,
)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "oro_lookup_company",
            "description": "Resolve a UK company by name. Costs 5 credits.",
            "parameters": {
                "type": "object",
                "properties": {"q": {"type": "string", "description": "Company name"}},
                "required": ["q"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "oro_company_profile",
            "description": "Full supplier profile: core record plus every public contract won. Costs 12 credits.",
            "parameters": {
                "type": "object",
                "properties": {"company_number": {"type": "string"}},
                "required": ["company_number"],
            },
        },
    },
]


def call_tool(name: str, args: dict) -> dict:
    if name == "oro_lookup_company":
        return oro.get("/companies/search", params={"name": args["q"]}).raise_for_status().json()
    if name == "oro_company_profile":
        return oro.get(f"/companies/{args['company_number']}/profile").raise_for_status().json()
    raise ValueError(name)


client = OpenAI()
messages = [
    {
        "role": "user",
        "content": "Look up the UK company 'Serco' and summarise its full supplier "
        "profile: contracts won, plus credits_charged and credits_remaining.",
    }
]

while True:
    response = client.chat.completions.create(model="gpt-4o", messages=messages, tools=TOOLS)
    msg = response.choices[0].message
    messages.append(msg)
    if not msg.tool_calls:
        print(msg.content)
        break
    for tc in msg.tool_calls:
        result = call_tool(tc.function.name, json.loads(tc.function.arguments))
        print(f"[{tc.function.name}] credits_charged={result.get('credits_charged')} "
              f"credits_remaining={result.get('credits_remaining')}")
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result)})

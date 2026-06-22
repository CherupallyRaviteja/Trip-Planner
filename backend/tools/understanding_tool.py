from email.mime import text
import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def understand_query(query, memory):

    prompt = f"""
    Current Memory:
    {memory}

    User Query:
    {query}

    Return JSON:

    {{
     "query_type": "",
      "trip_details": {{
        "destination": null,
        "duration_days": null,
        "budget": null,
        "companions": null
      }},
      "memory_updates": {{
        "budget_preference": null,
        "travel_style": null,
        "interests": [],
        "food_preferences": [],
        "transport_preferences": []
      }}
    }}

    Rules:
    - trip_request:
        - Any request to create, modify, update, continue, refine, or discuss a travel plan.
    - non_trip_request:
        -  Any query unrelated to travel planning or travel preferences.

    Only include information in memory_updates if it represents a long-term user preference.

    Do not store:
    - destination
    - trip budget
    - trip duration
    - current trip companions

    Store only recurring preferences.
    """

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json"
    }
)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    result = json.loads(text)
    trip = result["trip_details"]

    if trip["duration_days"] is not None:
        trip["duration_days"] = int(trip["duration_days"])

    if trip["budget"] is not None:
        trip["budget"] = int(trip["budget"])
    return result
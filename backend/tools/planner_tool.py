from google import genai
import os
from dotenv import load_dotenv
import json
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_plan(query,intent,weather,memory):

    prompt = f"""
    You are an AI Travel Planner.

    User Query:
    {query}

    Trip Details:
    {intent["trip_details"]}

    Weather:
    {weather}

    User Preferences:
    {memory}

    Return ONLY valid JSON.

    {{
    "budget_analysis": {{
        "sufficient": true,
        "recommended_budget": 0,
        "reason": ""
    }},

    "weather_advice": "",

    "itinerary": [
        {{
        "day": 1,
        "title": "",
        "image_query": "",
        "activities": [
            {{
            "name": "",
            "description": "",
            "tips": ""
            }}
        ]
        }}
    ]
    }}
    IMPORTANT:
    - All budgets are in Indian Rupees (INR) unless the user explicitly specifies another currency.

    Budget Analysis Rules:
    -  If the user's budget appears sufficient for the trip:
        - sufficient = true
        - recommended_budget = null

    - If the user's budget appears insufficient:
        - sufficient = false
        - recommended_budget = a realistic suggested budget
    - Only provide recommended_budget when the current budget is insufficient.
    - Base estimates on destination, duration and companions.

    Rules:
    - Return JSON only
    - Budget analysis must be realistic for the destination.
    - Weather advice should be based on the supplied weather data.
    - Generate exactly the same number of itinerary days as duration_days.
    - For each day generate a highly searchable image_query.
        Examples:
        - Goa beach sunset
        - Goa scuba diving
        - Paris Eiffel Tower
        - Kerala backwaters
        - Manali snow mountains`
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)
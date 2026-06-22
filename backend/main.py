from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os
from agent import travel_agent

# Load environment variables
load_dotenv()

# FastAPI App
app = FastAPI(
    title="TripPlanner API",
    description="AI Travel Planning Assistant",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://trip-planner-t5dv.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# System Prompt
SYSTEM_PROMPT = """
    You are an AI Travel Planner.

    Trip Details:
    {trip_details}

    Weather:
    {weather}

    User Memory:
    {memory}

    Rules:

    1. Estimate realistic accommodation, food and transport costs.
    2. Check if the user's budget is sufficient.
    3. If insufficient, suggest adjustments.
    4. Then generate the itinerary.
    5. Use user preferences from memory.
"""

# Request Model
class ChatRequest(BaseModel):
    message: str
    user_id: str

# Health Check
@app.get("/")
def health():
    return {
        "status": "online",
        "service": "TripPlanner API"
    }

# Chat Endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    result = travel_agent(req.message, user_id=req.user_id)
    return result
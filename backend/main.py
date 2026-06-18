from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os

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
        "https://trip-planner-t5dv.vercel.app",
        "http://localhost:5173"
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
You are TripPlanner, an AI Travel Planning Assistant.

You ONLY answer travel-related questions.

You help users with:
- Travel itineraries
- Destination recommendations
- Budget estimation
- Tourist attractions
- Transportation advice
- Accommodation suggestions
- Travel tips

If a question is unrelated to travel,
politely refuse and ask the user to ask a travel-related question.

Format responses clearly using headings and bullet points when appropriate.
"""

# Request Model
class ChatRequest(BaseModel):
    message: str

# Health Check
@app.get("/")
def health():
    return {
        "status": "online",
        "service": "TripPlanner API"
    }

# Chat Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\n\nUser: {request.message}"
        )

        return {
            "reply": response.text
        }

    except Exception as e:
        print("Error:", e)

        return {
            "reply": "Sorry, I couldn't process your request right now. Please try again."
        }
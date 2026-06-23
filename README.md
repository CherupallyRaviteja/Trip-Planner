# AI Travel Planner Agent

An intelligent AI-powered Travel Planning Agent that creates personalized travel itineraries, analyzes budgets, fetches real-time weather information, and remembers user preferences to provide better travel recommendations over time.

Built as part of the GENAI Internship Milestone 2 project.

---

## Overview

AI Travel Planner is an autonomous travel agent that goes beyond simple question-answering. The agent plans complete trips, retrieves destination weather information, remembers user travel preferences, and generates personalized travel recommendations based on previous interactions.

The system follows an agentic workflow consisting of planning, tool usage, memory management, and decision-making.

---

## Agent Capabilities

### 1. Multi-Step Task Planning & Execution

The agent breaks complex travel requests into multiple steps:

1. Understand user travel requirements.
2. Extract destination, duration, budget, and companions.
3. Analyze weather conditions.
4. Generate budget estimates.
5. Create a day-wise itinerary.
6. Personalize recommendations using stored preferences.

Example:

> "Plan a 7-day Goa trip with friends under ₹30,000"

The agent automatically creates a complete travel plan instead of answering with a single response.

---

### 2. Tool/API Integration

The agent integrates external APIs to enhance decision-making.

Features:

* Real-time weather information
* Destination-based recommendations
* Travel images for itinerary visualization
* API failure handling with fallback responses

APIs Used:

* OpenWeatherMap API (Weather Data)
* Pexels API (Destination Images)
* Gemini API (Planning and Reasoning)

---

### 3. Context Memory & Decision Making

The agent remembers user preferences across conversations.

Stored Preferences:

* Travel interests
* Food preferences
* Travel style
* Budget preferences
* Previous trips

Example:

User:

> "I like beaches and water sports."

Later:

> "Plan a trip for me."

The agent automatically incorporates beach destinations and water activities into recommendations.

---

## How It Works

### Step 1: User Request Analysis

The agent analyzes the user's message and extracts:

* Destination
* Budget
* Duration
* Companions
* Travel preferences

### Step 2: Memory Retrieval

The agent loads previously saved preferences and past trip information.

### Step 3: Planning

The system generates a structured travel plan including:

* Weather analysis
* Budget estimation
* Daily itinerary
* Activity recommendations

### Step 4: Tool Usage

External APIs are called to retrieve:

* Weather information
* Travel images

### Step 5: Personalized Response

The final itinerary is generated using both the current request and stored user preferences.

---

## Tech Stack

### Frontend

* React.js
* Tailwind CSS
* JavaScript

### Backend

* FastAPI
* Python

### AI Model

* Google Gemini

### Storage

* JSON-based User Memory

---

## Project Structure

```text
backend/
│
├── agent.py
├── main.py
├── planner.py
├── weather.py
├── memory.py
├── image_service.py
│
└── data/
    └── memories/

frontend/
│
├── src/
│   ├── components/
│   ├── services/
│   └── App.jsx
│
└── package.json
```

---

## System Architecture
```
┌──────────────────────────────────────────────┐
│                 USER INTERFACE               │
│                 React + Tailwind             │
└──────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                FastAPI Backend               │
│                  main.py                     │
└──────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               Travel Agent Core              │
│                 agent.py                     │
└──────────────────────────────────────────────┘
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Intent       │ │ User Memory  │ │ Planner      │
│ Extraction   │ │ Management   │ │ Engine       │
└──────────────┘ └──────────────┘ └──────────────┘
      │                │                │
      ▼                ▼                ▼

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Gemini API   │ │ JSON Memory  │ │ Weather API  │
│ Reasoning    │ │ Per User     │ │ OpenWeather  │
└──────────────┘ └──────────────┘ └──────────────┘
                                        │
                                        ▼

                              ┌──────────────┐
                              │ Pexels API   │
                              │ Images       │
                              └──────────────┘

                                        │
                                        ▼

                     ┌─────────────────────────┐
                     │ Personalized Travel Plan│
                     │ Budget + Weather +      │
                     │ Day-wise Itinerary      │
                     └─────────────────────────┘
```

---

## Agent Workflow

```
User Request
      │
      ▼
Extract Travel Details
      │
      ▼
Load User Memory
      │
      ▼
Merge Preferences
      │
      ▼
Fetch Weather Data
      │
      ▼
Generate Budget Analysis
      │
      ▼
Create Day-wise Itinerary
      │
      ▼
Fetch Destination Images
      │
      ▼
Return Personalized Travel Plan
---
## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/CherupallyRaviteja/Trip-Planner
cd AI-Travel-Planner
```
--- 

### 2. Backend Setup

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_key
OPENWEATHER_API_KEY=your_weather_key
PEXELS_API_KEY=your_pexels_key
```

Run Backend:

```bash
uvicorn main:app --reload
```

---

### 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Example Queries

### Travel Planning

```text
Plan a 5-day Goa trip with friends under ₹25,000
```

### Preference Memory

```text
I like beaches and water sports
```

### Trip Modification

```text
Make it 7 days instead
```

### Budget Analysis

```text
Plan a Sri Lanka trip under ₹40,000
```

---

## Deployment

Frontend URL:

```text
https://trip-planner-t5dv.vercel.app
```

Backend URL:

```text
https://trip-planner-1-4juy.onrender.com
```

---

## Output Screenshots

### Home Page

<img width="1348" height="609" alt="image" src="https://github.com/user-attachments/assets/cf7b5b12-4f8e-4ff9-a054-4e65cbd75fbe" />

<img width="1353" height="609" alt="image" src="https://github.com/user-attachments/assets/82ed77f4-cd9e-4073-95eb-ebc9a638d8a9" />

<img width="1353" height="606" alt="image" src="https://github.com/user-attachments/assets/8e73b41d-2c3e-42f8-9778-0aa1b74f42ed" />

### Response 

<img width="1354" height="609" alt="image" src="https://github.com/user-attachments/assets/1ffb7aa6-d684-405c-8191-1660f5fcee10" />

<img width="1350" height="607" alt="image" src="https://github.com/user-attachments/assets/9e89c440-44a7-4075-a597-2b6810c8c573" />

<img width="1353" height="608" alt="image" src="https://github.com/user-attachments/assets/cabe0b0b-fba9-406c-9c94-cd08c375f7a6" />

---

## Features Implemented

✔ Multi-Step Planning

✔ Weather API Integration

✔ Travel Image Integration

✔ Personalized Memory

✔ User-Specific Memory Storage

✔ Budget Analysis

✔ Day-wise Itinerary Generation

✔ API Failure Handling

✔ Domain Restriction (Travel Only)

---

## Future Improvements

* Hotel recommendations
* Flight price integration
* Interactive maps
* Restaurant recommendations
* Travel expense tracking
* Multi-city trip planning

---

## Author

Cherupally Raviteja

B.Tech – Artificial Intelligence & Machine Learning


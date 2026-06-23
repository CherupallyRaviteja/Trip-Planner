from memory import (load_memory,merge_memory,save_last_trip)
from tools.understanding_tool import understand_query
from tools.weather_tool import get_weather
from tools.planner_tool import generate_plan
from tools.image_tool import get_image

def travel_agent(query, user_id):

    status = []
    # 1. Load Memory

    memory = load_memory(user_id)

    # 2. Understand User Query
    try:
        intent = understand_query(query,memory)

    except Exception as e:
        print("Understanding Agent Error:", e)
        return {
            "status": ["Understanding Failed"],
            "message":"Unable to process your request right now. Please try again."
        }

    last_trip = memory.get("last_trip", {})

    trip = intent["trip_details"]   

    query_type = intent["query_type"]

    if query_type == "non_trip_request":

        memory = merge_memory(
            memory,
            intent["memory_updates"],
            user_id
        )

        if any(intent["memory_updates"].values()):

            return {
                "message":
                "Thank you. Your preferences have been saved and will be used for future trip recommendations."
            }

        return {
            "message":
            "I am Trip Planner. I can only generate trip plans and handle travel-related preferences."
        }

   
    for key, value in last_trip.items():
        if trip.get(key) is None:
            trip[key] = value

    print(intent)

    print("\n===== INTENT =====")
    print(intent)

    # 3. Update Memory
    print("\n===== MEMORY UPDATES =====")   
    print(type(intent))
    print(intent["memory_updates"])
    
    save_last_trip(memory,intent["trip_details"],user_id)

    print("\n===== UPDATED MEMORY =====")
    print(memory)

    # 4. Extract Destination
    destination = intent["trip_details"]["destination"]

    # 5. Weather Tool
    if destination:
        try:
            weather = get_weather(intent["trip_details"]["destination"])
            status.append("Weather Retrieved")

        except Exception as e:
            print("Weather API Error:",e)
            weather = {
                "city": intent["trip_details"]["destination"],
                "temperature": None,
                "condition": "Unavailable",
                "humidity": None,
                "wind_speed": None
            }
            status.append("Weather Service Unavailable")

    else:
        weather = None

    print("\n===== WEATHER =====")
    print(weather)

    # 6. Budget Tool
    duration = intent["trip_details"]["duration_days"]

    # 7. Planner Agent
    try:
        plan = generate_plan(query,intent,weather,memory)

        for day in plan["itinerary"]:
            image = get_image(day["image_query"])
            day["image"] = image
            print(day)
    except Exception as e:
        print("Planner Error:",e)
        return {
            "status": ["Planning Failed"],
            "trip_details":intent["trip_details"],
            "message":"Travel plan generation is temporarily unavailable."
        }

    # 8. Status Tracking
    status = ["Memory Loaded","Query Understood","Memory Updated"]

    if weather:
        status.append("Weather Retrieved")

    status.append("Travel Plan Generated")

    # 9. Final Response
    print("\n===== STATUS =====")
    
    return {
    "status": status,
    "trip_details": intent["trip_details"],
    "weather": weather,
    **plan
    }   

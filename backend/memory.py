import json
import os

MEMORY_DIR = r"D:/Python Projects/TripPlanner/backend/data/memories"


def load_memory(user_id):

    os.makedirs(
        MEMORY_DIR,
        exist_ok=True
    )

    memory_file = os.path.join(
        MEMORY_DIR,
        f"{user_id}.json"
    )

    if not os.path.exists(memory_file):
        return {}

    with open(memory_file, "r") as f:
        return json.load(f)


def save_memory(memory, user_id):

    os.makedirs(
        MEMORY_DIR,
        exist_ok=True
    )

    memory_file = os.path.join(
        MEMORY_DIR,
        f"{user_id}.json"
    )

    print("Saving to:", memory_file)

    with open(memory_file, "w") as f:
        json.dump(
            memory,
            f,
            indent=4
        )


def merge_memory(memory,updates,user_id):

    print("CURRENT MEMORY:", memory)
    print("UPDATES:", updates)

    for key, value in updates.items():

        if value is None:
            continue

        if value == []:
            continue

        if isinstance(value, list):

            existing = set(
                memory.get(key, [])
            )

            existing.update(value)

            memory[key] = list(existing)

        else:

            memory[key] = value

    print("FINAL MEMORY:", memory)

    save_memory(
        memory,
        user_id
    )

    return memory


def save_last_trip(
    memory,
    trip_details,
    user_id
):

    destination = trip_details.get(
        "destination"
    )

    if not destination:
        return

    memory["last_trip"] = trip_details

    save_memory(
        memory,
        user_id
    )
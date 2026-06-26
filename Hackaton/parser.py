
import json
from datetime import datetime

def load_and_parse(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    for task in tasks:
        task["deadline"] = datetime.strptime(
            task["deadline"],
            "%Y-%m-%d"
        )

    return tasks
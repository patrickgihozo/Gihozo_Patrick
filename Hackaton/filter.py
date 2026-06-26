from datetime import datetime, timedelta

def tasks_due_soon(tasks):
    today = datetime.today()
    next_three_days = today + timedelta(days=3)

    return [
        task
        for task in tasks
        if today <= task["deadline"] <= next_three_days
    ]
def linear_search(tasks, target):
    for task in tasks:
        if task["name"] == target:
            return task

    return None

def build_index(tasks):
    return {
        task["name"]: task
        for task in tasks
    }


def find_task(task_index, task_name):
    return task_index.get(task_name)


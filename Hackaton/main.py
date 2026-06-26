from parser import load_and_parse
from sorter import sort_tasks
from filter import tasks_due_soon
from search import build_index, find_task
from benchmark import benchmark


def main():

    # Load JSON and parse dates
    tasks = load_and_parse(
    r"C:\Users\User\Downloads\tasks_100000.json"
)

    print(f"Loaded {len(tasks)} tasks")

    # Sort
    sorted_tasks = sort_tasks(tasks)

    print("\nTop 5 Sorted Tasks")

    for task in sorted_tasks[:5]:
        print(task)

    # Filter
    due_soon = tasks_due_soon(tasks)

    print(f"\nTasks due within 3 days: {len(due_soon)}")

    # Build HashMap
    task_index = build_index(tasks)

    # Search
    task = find_task(task_index, "Task_500")

    print("\nSearch Result")

    print(task)

    # Benchmark
    benchmark(tasks, task_index)


if __name__ == "__main__":
    main()
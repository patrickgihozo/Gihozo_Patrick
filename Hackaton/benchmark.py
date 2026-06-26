import time
from search import linear_search

def benchmark(tasks, task_index):

    target = "Task_99999"

    start = time.perf_counter()

    linear_search(tasks, target)

    linear_time = time.perf_counter() - start

    start = time.perf_counter()

    task_index.get(target)

    dict_time = time.perf_counter() - start

    print("\n===== BENCHMARK RESULTS =====")
    print(f"Linear Search : {linear_time:.8f} seconds")
    print(f"Dictionary Lookup : {dict_time:.8f} seconds")
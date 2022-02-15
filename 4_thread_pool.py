import time
from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(8)


def handle_result(result):
    print(f'Got the result: {result.result()}')


def func(x, y):
    time.sleep(5)
    return x + y


future = pool.submit(func, 2, 3)

future.add_done_callback(handle_result)



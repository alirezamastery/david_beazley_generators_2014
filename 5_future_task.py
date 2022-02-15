import time
from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(8)


class Task:

    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None):
        # Run to the next yield
        try:
            fut = self._gen.send(value)
            # Future returned:
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        # Handling of results:
        result = fut.result()
        self.step(result)  # Feedback loop (run to next yield)


def func(x, y):
    time.sleep(5)
    return x + y


def do_func(x, y):
    result = yield pool.submit(func, 2, 3)
    print(f'Got: {result}')


g = do_func(2, 3)
t = Task(g)
t.step()


# def example(n):
#     while n > 0:
#         result = yield pool.submit(func, n, n)
#         print(f'Got: {result}')
#         n -= 1
#
#
# Task(example(10)).step()

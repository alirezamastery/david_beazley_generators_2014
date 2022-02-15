from concurrent.futures import Future
import time
from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(8)


def __iter__(self):
    if not self.done():
        yield self
    return self.result()


Future.__iter__ = __iter__


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


def after(delay, gen):
    yield pool.submit(time.sleep, delay)

    yield from gen


def func(x, y):
    time.sleep(5)
    return x + y


def do_func(x, y):
    result = yield pool.submit(func, 2, 3)
    print(f'Got: {result}')


Task(after(5, do_func(2, 3))).step()

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


def recursive(n):
    yield pool.submit(time.sleep, 0.001)
    Task(recursive(n + 1)).step()
    print(n)


gen = recursive(1)

Task(gen).step()

from collections import deque


_registry = {}
_msg_queue = deque()


def send(name, msg):
    _msg_queue.append((name, msg))


def run():
    while _msg_queue:
        name, msg = _msg_queue.popleft()
        _registry[name].send(msg)


def actor(func):
    def wrapper(*ags, **kwargs):
        gen = func(*ags, **kwargs)
        next(gen)
        _registry[func.__name__] = gen

    return wrapper


@actor
def printer():
    while True:
        item = yield
        print(f'Got: {item}')


@actor
def ping():
    while True:
        msg = yield  # Get a message
        print(f'ping: {msg}')
        send('pong', msg + 1)


@actor
def pong():
    while True:
        msg = yield  # Get a message
        print(f'pong: {msg}')
        send('ping', msg + 1)


printer()  # this line is necessary

send('printer', 'hello')
send('printer', 'asdgfj')
ping()
pong()

send('ping', 0)

# generator has 'gi_running' attribute set to True when it is running

run()

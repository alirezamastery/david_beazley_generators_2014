_registry = {}


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


printer()  # this line is necessary


def send(name, msg):
    _registry[name].send(msg)


send('printer', 'hello')

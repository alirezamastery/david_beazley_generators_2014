def spam():
    while True:
        item = yield
        print(f'Got: {item}')


s = spam()

next(s)  # make it advance to the yield statement

s.send('hello')
s.send('ok 123')

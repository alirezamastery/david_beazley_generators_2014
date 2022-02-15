def chain(x, y):
    yield from x
    yield from y


a = [1, 2, 3]
b = [4, 5, 6]
for n in chain(a, b):
    print(n)

for n in chain(chain(a, b), chain(b, b)):
    print(n, end=' ')


"""
get = generator()

next(get)
gen.send(item)
gen.close()
gen.throw(exc, val, tb)  -> can by caught in the generator
result = yield from gen
"""
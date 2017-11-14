def simple_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        print('do something before function call')
        r = func(*args, **kwargs)
        print(r)
        print('do something after function call')
        return r

    return wrapper


@simple_decorator
def test(x, y):
    return x + y


def factorial(n):
    z, i = 1, 1
    while i <= n:
        z = z * i
        yield z
        i = i + 1


def coroutine(coro_func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        r = coro_func(*args, **kwargs)
        next(r)
        return r
    return wrapper


@coroutine
def coro():
    while True:
        x = (yield)
        if x and type(x) == int:
            print('ho ho ho')
        else:
            print('no buddy')


rules = []


def assign_rule(func, *args, **kwargs):
    rules.append(func)

    def wrapper():
        return func(*args, **kwargs)

    return wrapper


@assign_rule
def sum_rule(x, y):
    return x + y


@assign_rule
def mul_rule(x, y):
    return x * y


if __name__ == '__main__':
    f = factorial(10)
    print(next(f))
    print(next(f))
    print(next(f))
    c = coro()
    next(c)
    c.send(10)
    c.send('x')
    print(rules)

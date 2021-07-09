import functools


def count_dec(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывается в {count} раз')
        result = func(*args, **kwargs)
        return result
    return wrapper


@count_dec
def test1():
    print('hello')


# for _ in range(3):
#     test1()

print(dir(__builtins__))

def func_1(x):
    return x + 10


def func_2(func, *args, **kwargs):
    a = func(*args, **kwargs)
    b = func(*args, **kwargs)
    c = a * b
    return c


rez = func_2(func_1, 9)
print(rez)

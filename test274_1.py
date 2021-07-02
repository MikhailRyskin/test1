import functools


def bread(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(' --------- ')
        func(*args)
        print('\_______/')

    return wrapped_func


def ingradients(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(' салат ')
        func(*args)
        print('помидоры')
    return wrapped_func


@ingradients
@bread
def meet(sort_meet: str) -> None:
    """
    Выводит начинку гамбургера
    :param sort_meet:
    :return:
    """
    print(sort_meet)


meet('буженина')
print(meet.__name__, meet.__doc__)

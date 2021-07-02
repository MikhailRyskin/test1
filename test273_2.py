import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    """
    Декоратор, который выводит время выполнения декорируемой функции
    :param func:
    :return:
    """
    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args)
        finish_time = time.time()
        func_time = finish_time - start_time
        print(f'Функция выполнялась {round(func_time, 2)}')
        return result
    return wrapped_func


@timer
def hard_func(number):
    result = 0
    for _ in range(number):
        result += sum(i ** 2 for i in range(1, 10000))
    return result


res = hard_func(300)
print(res)

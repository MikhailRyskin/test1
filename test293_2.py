import functools
import time
from typing import Callable, Any


def wait_with_number(_func=None, *,  number: int = 3) -> Callable:
    def wait_n_sec(func: Callable) -> Any:
        """
        Декоратор, делающий паузу в number сек перед выполнением декорируемой функции.
        Если аргумент не передаётся, пауза в 3 секунды по умолчанию.
        :param func:
        :return:
        """
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            time.sleep(number)
            result = func(*args, **kwargs)
            return result
        return wrapped_func
    if _func is None:
        return wait_n_sec
    else:
        return wait_n_sec(_func)


@wait_with_number(number=8)
def test() -> None:
    print('Выполнение тестовой функции')


# @wait_with_number
# def test() -> None:
#     print('Выполнение тестовой функции')


print(round(time.time(), 4))
test()
print(round(time.time(), 4))

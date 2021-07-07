from typing import Callable, Any


def do_any_with_number(number: int) -> Callable:
    def do_any_decorator(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapped_func
    return do_any_decorator


@do_any_with_number(3)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')

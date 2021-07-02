from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register(func):
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Привет, {name}'


@register
def say_goodbye(name):
    return f'Прощай, {name}'


print(PLUGINS)
print(say_hello('Lion'))

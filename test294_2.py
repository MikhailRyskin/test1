import functools
from typing import Callable, Any
import datetime


# def debug(func: Callable) -> Any:
#     """
#     Декоратор, который выводит название, аргументы и результат декорируемой функции.
#     :param func:
#     :return:
#     """
#
#     @functools.wraps(func)
#     def wrapped_func(*args, **kwargs):
#         args_kwargs = ','.join(f'"{str(elem)}"' for elem in args)
#         for key, value in kwargs.items():
#             args_kwargs += f',{key}={value} '
#         print(f'Вызывается {func.__name__}({args_kwargs})')
#         result = func(*args, **kwargs)
#         print(f'"{func.__name__}" вернула значение "{result}"')
#         return result
#
#     return wrapped_func


def logging(func: Callable) -> Any:
    """
    Декоратор. Выводит название функции и её документацию. Если во время выполнения
    Если во время выполнения декорируемой функции возникла ошибка,
    то в файл function_errors.log записываются название функции, название ошибки, дата и время возникновения ошибки.
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'\nвыполняется функция: {func.__name__}{func.__doc__}')
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_str = f'функция:{func.__name__}, ошибка: {exc}, время:{datetime.datetime.now()}\n'
                log_file.write(log_str)

    return wrapped_func


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса.
    :param decorator:
    :return:
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__'):
                cur_method = getattr(cls, method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate


@for_all_methods(logging)
class Square:
    """
    Класс, описывающий квадрат. Задаётся стороной квадрата.
    Методы позволяют вычислять периметр и площадь.
    """

    def __init__(self, length: float) -> None:
        self._length = length
        self.square = 0
        self.perimeter = 0

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    def square_per(self) -> float:
        """
        документация метода square_per
        :return:
        """
        self.perimeter = self._length * 4
        return self.perimeter

    def square_sq(self) -> float:
        """
        документация метода square_sq
        :return:
        """
        self.square = self._length ** 2
        return self.square


sq_1 = Square(5)
print(sq_1.square_sq())
print(sq_1.square_per())

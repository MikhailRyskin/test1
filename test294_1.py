import datetime
import math
import functools
import time
from typing import Callable, Any


def create_time(cls):
    """
    Декоратор класса. Выводит время создание экземпляра класса и название класса.
    :param cls:
    :return:
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(f'время создания экземпляра класса "{cls.__name__}": {datetime.datetime.now()}')
        print('методы класса:', end='')
        for method in dir(cls):
            if not method.startswith('__'):
                print(method, end=' ')
        print()
        return instance
    return wrapper


@create_time
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
        self.perimeter = self._length * 4
        return self.perimeter

    def square_sq(self) -> float:
        self.square = self._length ** 2
        return self.square


@create_time
class Triangle:
    """
    Класс, описывающий треугольник. Задаётся длиной основания и высотой.
    Методы позволяют вычислять периметр и площадь.
    """

    def __init__(self, length: float, height: float) -> None:
        self._length = length
        self._height = height
        self.square = 0
        self.perimeter = 0

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    def triangle_per(self) -> float:
        self.perimeter = math.sqrt((self._length / 2) ** 2 + self._height ** 2) * 2 + self._length
        return self.perimeter

    def triangle_sq(self) -> float:
        self.square = self._length * self._height / 2
        return self.square


sq_1 = Square(5)
time.sleep(5)
sq_2 = Square(length=8)
time.sleep(3)
triangle_1 = Triangle(10, 6)

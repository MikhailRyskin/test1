import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(path: str) -> Iterator:
    dir_name = os.getcwd()
    print('текущая директория при входе:', dir_name)
    try:
        os.chdir(path)
        print('поменяли текущую директорию на:', path)
    except FileNotFoundError as exc:
        print('такого пути нет:', exc)
    finally:
        yield
        os.chdir(dir_name)
        print('в конце текущая директория:', os.getcwd())


with in_dir('C:\Миша'):
    print(os.listdir())

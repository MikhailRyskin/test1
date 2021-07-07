import time
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def timer() -> Iterator:
    start_time = time.time()
    try:
        yield
    except Exception as exc:
        print('Было исключение', exc)
    finally:
        print(time.time() - start_time)


with timer() as t1:
    result = 0
    for _ in range(100):
        result += sum(i ** 2 for i in range(1, 10000))
    result += 'hgf'
    print(result)

with timer() as t2:
    result = 0
    for _ in range(500):
        result += sum(i ** 2 for i in range(1, 10000))
    print(result)

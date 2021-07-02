import time


def timer(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args)
    finish_time = time.time()
    func_time = finish_time - start_time
    print(f'Функция выполнялась {round(func_time, 2)}')
    return result


def hard_func(number):
    result = 0
    for _ in range(number):
        result += sum(i ** 2 for i in range(1, 10000))
    return result


res = timer(hard_func, 500)
print(res)

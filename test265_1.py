# def my_generator():
#     count = 0
#     while True:
#         yield count
#         count += 1
#
#
# for number in my_generator():
#     print(number)

def prime_numbers_generator(n):
    """
    генератор простых чисел
    :param n: верхняя граница диапазона
    :return:
    """
    end = n
    start = 1
    prime_numbers = []
    while start < end:
        start += 1
        for prime in prime_numbers:
            if start % prime == 0:
                break
        else:
            prime_numbers.append(start)
            yield start


range_1 = 50

for number in prime_numbers_generator(range_1):
    print(number, end=' ')


def fibonacci(f_number):
    """
    генератор чисел Фибоначчи
    :param f_number: верхняя граница диапазона
    :return:
    """
    cur_number = 0
    next_number = 1
    for _ in range(f_number):
        yield cur_number
        cur_number, next_number = next_number, cur_number + next_number


print()
for num in fibonacci(12):
    print(num, end=' ')

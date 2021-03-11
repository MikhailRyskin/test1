import random

n = int(input('Введите кол-во чисел: '))
my_list = [random.randint(0, 10) for _ in range(n)]
a = int(input('Введите а: '))
b = int(input('Введите b: '))
print(my_list)
my_list[a:b + 1] = []
print(my_list)

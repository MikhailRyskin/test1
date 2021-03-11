import random


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21,
          2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29,
          8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
set_1 = set(nums_1)
set_2 = set(nums_2)
print('1-е множество:', set_1)
print('2-е множество:', set_2)
print('Минимальный элемент 1-го множества:', min(set_1))
print('Минимальный элемент 1-го множества:', min(set_1))
set_1.discard(min(set_1))
set_2.discard(min(set_2))
rand_1 = random.randint(100, 200)
rand_2 = random.randint(100, 200)
print('Случайное число для 1-го множества: ', rand_1)
print('Случайное число для 1-го множества: ', rand_2)
set_1.add(rand_1)
set_2.add(rand_2)
print('Объединение множеств:', set_1.union(set_2))
print('Пересечение множеств:', set_1.intersection(set_2))
print('Элементы, входящие в nums_2, но не входящие в nums_1:', set_2.difference(set_1))

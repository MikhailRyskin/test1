import random


abc = tuple('а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split())
list_1 = [random.choice(abc) for _ in range(10)]
list_2 = [random.choice(abc) for _ in range(10)]
print('Первый список:', list_1)
print('Второй список:', list_2)
dict_1 = {ind: letter for ind, letter in enumerate(list_1)}
dict_2 = {ind: letter for ind, letter in enumerate(list_2)}
print('Первый словарь:', dict_1)
print('Первый словарь:', dict_2)

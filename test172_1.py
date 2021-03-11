a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
list_cube = [x**3 for x in range(a, b + 1)]
list_square = [x**2 for x in range(a, b + 1)]
print('Список кубов чисел в диапазоне от', a, 'до', b, ':', list_cube)
print('Список квадратов чисел в диапазоне от', a, 'до', b, ':', list_square)

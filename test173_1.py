a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
list_even = [x for x in range(a, b + 1) if x % 2 == 0]
print(list_even)

num = int(input('Введите целое число: '))
num_dict = dict()
for num_key in range(1, num + 1):
    num_dict[num_key] = num_key**2
print('Результат', num_dict)

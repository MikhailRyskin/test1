count = int(input('Кол-во чисел в списке: '))
numbers_list = []
for i in range(count):
    print('Введите', i + 1, 'число:', end=' ')
    number = int(input())
    numbers_list.append(number)
dev = int(input('Введите делитель: '))
sum_i = 0
for i in range(count):
    if numbers_list[i] % dev == 0:
        sum_i += i
        print('Индекс числа', numbers_list[i], ':', i)
print('Сумма индексов:', sum_i)

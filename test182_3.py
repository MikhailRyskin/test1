print('Введите 4 числа от 0 до 255.')
numb_list = []
for i in range(1, 5):
    numb = int(input(f'Введите {i} число: '))
    while numb < 0 or numb > 255:
        print('Ошибка ввода!')
        numb = int(input(f'Введите {i} число: '))
    numb_list.append(numb)
ip_address = '{0}.{1}.{2}.{3}'.format(numb_list[0], numb_list[1], numb_list[2], numb_list[3])
print('IP-aдрес:', ip_address)

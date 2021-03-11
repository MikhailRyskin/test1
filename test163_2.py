first_msg = list(input('Первое сообщение: '))
second_msg = list(input('Второе сообщение: '))
if first_msg.count('!') > second_msg.count('?'):
    first_msg.extend(second_msg)
    print(*first_msg, sep='')
elif first_msg.count('!') < second_msg.count('?'):
    second_msg.extend(first_msg)
    print(*second_msg, sep='')
else:
    print('Ой')


text = input('Введите строку: ')
i_num = int(input('Номер символа: ')) - 1
text_list = list(text)
overlap = 0
if i_num == 0:
    left = text_list[0]
else:
    left = text_list[i_num - 1]
print('Символ слева:', left)
if left == text_list[i_num]:
    overlap += 1
if i_num == len(text_list) - 1:
    right = text_list[i_num]
else:
    right = text_list[i_num + 1]
if right == text_list[i_num]:
    overlap += 1
print('Символ справа:', right)
if overlap == 1:
    print('Есть ровно один такой же символ.')
elif overlap == 2:
    print('Есть два таких-же символа.')
else:
    print('Таких-же символов нет.')

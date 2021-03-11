text = input('Введите текст: ')
text_list = list(text)
new_text_list = []
count = 0
for symbol in text_list:
    if symbol == ':':
        symbol = ';'
        count += 1
    new_text_list.append(symbol)
print('Исправленная строка:', end='')
for symbol in new_text_list:
    print(symbol, end='')
print('\nКол-во замен:', count)

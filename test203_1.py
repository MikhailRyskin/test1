text = input('Введите текст: ')
for ind, symbol in enumerate(text):
    if symbol == '~':
        print(ind, end=' ')
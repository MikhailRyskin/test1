text = input('Введите строку: ')
text_set = set(text)
dif_didgit = set()
for sym in text_set:
    if '0' <= sym <= '9':
        dif_didgit.add(sym)
print('Различные цифры строки:', *dif_didgit)

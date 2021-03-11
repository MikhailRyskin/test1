def gist(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist_dict = gist(text)
for i_sym in sorted(hist_dict.keys()):
    print(i_sym, ':', hist_dict[i_sym])
print('Максимальная частота:', max(hist_dict.values()))

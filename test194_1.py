punct_marks = {'.', ',', ';', ':', '!', '?'}
text = input('Введите строку: ')
count = 0
for sym in text:
    if sym in punct_marks:
        count += 1
print(count)
# text_set = set()
# for sym in text:
#     text_set.add(sym)
# print(punct_marks)
# print(text_set)
# h = punct_marks.intersection(text_set)
# print(h)
# print('Количество знаков пунктуации:', len(punct_marks.intersection(text_set)))

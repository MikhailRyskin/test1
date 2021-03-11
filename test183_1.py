word_list = ['зенит', 'спартак', 'динамо']
text = input('Введите текст: ')
text_list = text.split()
print(text_list)
count = 0
for word in word_list:
    count += text_list.count(word)
print(count)

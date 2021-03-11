word_list = []
word_count = [0, 0, 0]
for i in range(3):
    print('Введите', i + 1, 'слово: ', end='')
    word = input()
    word_list.append(word)
word = input('Слово из текста: ')
while word != 'end':
    for i in range(3):
        if word == word_list[i]:
            word_count[i] += 1
    word = input('Слово из текста: ')
for i in range(3):
    print(word_list[i], ':', word_count[i])

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ').lower()
k = int(input('Введите сдвиг: '))
encrypted_list = [alphabet[(alphabet.index(letter) + k) % 33] if letter != ' ' else ' ' for letter in text]
encrypted_text = ''.join(encrypted_list)
print('Зашифрованное сообщение:', encrypted_text)

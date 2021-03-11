text = input('Введите строку: ')
lower_count = 0
for letter in text:
    if letter.islower():
        lower_count += 1
if lower_count >= len(text)//2:
    print(text.lower())
else:
    print(text.upper())

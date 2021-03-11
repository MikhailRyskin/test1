phone_book = {}
while True:
    surname = input('Введите фамилию(end для выхода): ').title()
    if surname == 'End':
        print('Ввод окончен')
        break
    else:
        name = input('Введите имя: ').title()
        person = (surname, name)
        if person not in phone_book:
            phone_number = int(input('Введите номер телефона: '))
            phone_book[person] = phone_number
        else:
            print('Контакт уже есть в книге')
print(phone_book)

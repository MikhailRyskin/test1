data = {

    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')

}

passport_series = int(input('Введите серию паспорта: '))
passport_number = int(input('Введите номер паспорта: '))
passport = (passport_series, passport_number)
# if passport in data:
#     surname, name = data[passport]
#     print(surname, name)
# else:
#     print('Нет таких номера и серии паспорта')
surname, name = data.get(passport, ('Нет таких номера и серии паспорта', ''))
print(surname, name)

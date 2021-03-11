contact_dict = dict()
while True:
    print('Текущие контакты на телефоне:')
    for name in contact_dict:
        print(name, contact_dict[name])
    name = input('Введите имя: ')
    if name == 'end':
        print('Ввод завершён.')
        break
    elif name in contact_dict:
        print('Ошибка: такое имя уже существует.')
    else:
        contact_dict[name] = input('Введите номер телефона: ')

def ask_user(question, complaint='Неверный ввод', retries=3):
    while True:
        answer = input(question).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Количество попыток истекло')
            break
        print(complaint)
        print('Осталось попыток:', retries)


ask_user('Хотите выйти? ', 'Плохо')

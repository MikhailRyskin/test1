def if_film_exist(movie, films_list):
    for film in films_list:
        if movie == film:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица']
my_list = []

while True:
    print('\nТекущий топ фильмов:', my_list)
    new_movie = input('Введите название фильма: ')
    if if_film_exist(new_movie, films):
        print('Команды: добавить, вставить, удалить.')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_movie)
        elif command == 'удалить':
            if if_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('Этого фильма нет в вашем рейтинге.')
        elif command == 'вставить':
            if if_film_exist(new_movie, my_list):
                print('Этот фильм уже есть в вашем списке.')
            else:
                rate = int(input('На какое место добавить? '))
                my_list.insert(rate - 1, new_movie)
        else:
            print('Неверная команда!')
    else:
        print('Такого фильма нет на сайте')

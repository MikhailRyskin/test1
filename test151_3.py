id_numbers_list = []
k = int(input('Кол-во сотрудников в офисе: '))
for _ in range(k):
    id = int(input('ID сотрудника: '))
    id_numbers_list.append(id)
id_search = int(input('Какой ID ищем? '))
working = False
for id in id_numbers_list:
    if id == id_search:
        working = True
        break
if working:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')

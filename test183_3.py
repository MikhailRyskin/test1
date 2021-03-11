template = input('Введите шаблон (содержит {name} и {age}:) ')
while True:
    if '{name}' in template and '{age}' in template:
        break
    else:
        print('Нет одного или двух обязательных полей')
        template = input('Введите шаблон (содержит {name} и {age}: ')
people = input('Список людей через запятую: ')
people_list = people.split(', ')
ages = input('Возраст людей через пробел: ')
ages_list = ages.split()
print(people_list, ages_list)
for i_man in range(len(people_list)):
    print(template.format(name=people_list[i_man], age=ages_list[i_man]))
all_str = ', '.join(
    [' '.join([people_list[i_man], ages_list[i_man]]) for i_man in range(len(people_list))]
    )
print('Именинники:', all_str)

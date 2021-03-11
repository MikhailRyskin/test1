total_num = int(input('Кол-во участников: '))
command_num = int(input('Кол-во человек в команде: '))
members = []
if total_num % command_num != 0:
    print(total_num, 'участников невозможно поделить на команды по', command_num, 'человек!')
else:
    command = 1
    for _ in range(total_num // command_num):
        members.append(list(range(command, command + command_num)))
        command += command_num
    print('Общий список команд:', members)

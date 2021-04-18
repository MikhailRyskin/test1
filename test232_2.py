names = 'abcdefghijklmnop'
try:
    file = open('ages.txt', 'r')
    result_file = open('result.txt', 'w')
    count = 0
    for line in file:
        content = f'{names[count]} {int(line)}\n'
        result_file.write(content)
        count += 1
    file.close()
    result_file.close()
except FileNotFoundError:
    print('такого файла не существует')
except FileExistsError:
    print('попытка создания файла или директории, которая уже существует.')
except IsADirectoryError:
    print('ожидался файл, но это директория')
except ValueError:
    print('некорректное значения')

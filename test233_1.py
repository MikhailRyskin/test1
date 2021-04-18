CONST = 10
try:
    result_file = open('result231.txt', 'x')
    line = input('Введите строку: ')
    summ = int(line) + CONST
    result_file.write(str(summ))
except FileExistsError:
    print('файл уже существует')
except ValueError:
    print('Нельзя преобразовать данные в целое')
except Exception:
    print('Неожиданная ошибка')
else:
    print('Успешная запись')
# finally:
#     result_file.close()
#     print(result_file.closed)


import os


def find_file(cur_path, file_name):
    print('переходим', cur_path)

    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        print('  смотрим', path)
        if file_name == elem:
            return path
        if os.path.isdir(path):
            print('это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


# file_path = find_file(os.path.abspath(os.path.join('..', 'lessons')), '05_save')
# if file_path:
#     print('Абсолютный путь к файлу', file_path)
# else:
#     print('Файл не найден')


# check_path = os.path.abspath(os.path.join('..', '..', 'pythonbasic'))
# check_path = os.path.abspath(os.path.sep)
check_path = os.path.abspath(os.path.join('C:/', 'Книги'))

for dirpath, dirnames, filenames in os.walk(check_path):
    # print(dirpath, dirnames, filenames)
    for file in filenames:
        # if file == 'main.py':
        # if 'test15' in file or 'les14' in file:
        if 'Гэлбрейт' in file:
            print(os.path.join(dirpath, file))


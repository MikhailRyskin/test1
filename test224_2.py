import os


def find_all_py_files(check_path):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(check_path):
        for file in filenames:
            if '.py' in file:
                path = os.path.join(dirpath, file)
                files_list.append(path)
    return files_list


my_path = os.path.abspath(os.path.join('/', 'Skillbox', 'PythonBasic', 'Lessons', 'Module20'))

py_files = find_all_py_files(my_path)

# print(py_files)
out_file = open('scripts.txt', 'w+', encoding='utf8')
number_file = 1
for file in py_files:
    in_file = open(file, 'r', encoding='utf8')
    content = f'\nфайл {number_file}\n\n' + in_file.read() + '*'*40
    in_file.close()
    out_file.write(content)
    number_file += 1
out_file.close()

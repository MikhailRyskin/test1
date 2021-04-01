import os
import random


def find_all_files(check_path, file_name):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(check_path):
        for file in filenames:
            if file == file_name:
                path = os.path.join(dirpath, file)
                files_list.append(path)
    return files_list


my_path = os.path.abspath(os.path.join('/', 'Skillbox', 'PythonBasic', 'Lessons', 'Module21'))
my_file = 'main.py'
files = find_all_files(my_path, my_file)

random_file = random.choice(files)
print_file = open(random_file, 'r', encoding='utf8')
text = print_file.read()
print(text)
print_file.close()

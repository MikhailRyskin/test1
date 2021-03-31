import os

my_object = 'test1'
obj_path = os.path.abspath(os.path.join('..', my_object))
print(obj_path)
if os.path.exists(obj_path):
    if os.path.isfile(obj_path):
        size = os.path.getsize(obj_path)
        print(f'Это файл. Размер {size} байт')
    elif os.path.isdir(obj_path):
        print('Это директория')
    elif os.path.islink(obj_path):
        print('Это ссылка')
else:
    print('Такого объекта не существует')

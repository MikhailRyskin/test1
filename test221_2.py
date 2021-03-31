import os

my_dir = 'weblayout'
dir_path = os.path.abspath(os.path.join('..', '..', my_dir))
print(dir_path)
for elem in os.listdir(dir_path):
    path = os.path.abspath(os.path.join(dir_path, elem))
    print(path)

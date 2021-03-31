import os


rel_path = os.path.join('access', 'admin.bat')
print(rel_path)
abs_path = os.path.abspath(os.path.join('access', 'admin.bat'))
print(abs_path)

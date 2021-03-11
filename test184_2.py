disk = input('На каком диске должен лежать файл: ').upper()
extension = input('Требуемое расширение файла: ').lower()
path = '{0}:/user/docs/folder/new_file.{1}'.format(disk, extension)
if not path.startswith('C'):
    print('Указан не диск С')
elif not path.endswith('txt'):
    print('Указано расширение не txt')
else:
    print('Путь корректен!', path)

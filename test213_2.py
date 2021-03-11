data = 8

mutable = True
print('Тип данных:', end=' ')
if type(data) == int:
    print('int (целые)')
    mutable = False
elif type(data) == float:
    print('float (вещественные)')
    mutable = False
elif type(data) == bool:
    print('boolean (логический тип данных)')
    mutable = False
elif type(data) == str:
    print('str (строка)')
    mutable = False
elif type(data) == tuple:
    print('tuple (кортеж)')
    mutable = False
elif type(data) == list:
    print('list (список)')
elif type(data) == set:
    print('set (множество)')
elif type(data) == dict:
    print('dict (словарь)')

if mutable:
    print('Изменяемый (mutable)')
else:
    print('Неизменяемый (immutable)')
print('Id объекта:', id(data))

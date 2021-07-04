class Example:
    def __init__(self):
        print('вызов __init')
        pass

    def __enter__(self):
        print('вызов __enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('вызов __exit')
        if exc_type:
            print(f'тип ошибки: {exc_type}\nзначение ошибки: {exc_val}\n след ошибки {exc_tb}')
        return True


my_obj = Example()
with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
    print('Я обязательно выведусь...')


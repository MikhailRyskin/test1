def do_twice(func):
    def wrapped_func(*args, **kwargs):
        func(*args)
        func(*args)
    return wrapped_func


@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')

def do_any_with_number(number: int):
    def do_any_decorator(func):
        def wrapped_func(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapped_func
    return do_any_decorator


@do_any_with_number(5)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')



def do_twice(func):
    def wrapped_func(*args, **kwargs):
        func(*args)
        func(*args)
    return wrapped_func


@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
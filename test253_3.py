class DivisionError(Exception):
    pass


with open('numbers.txt', 'r') as file:
    for line in file:
        a, b = line.split()
        a = int(a)
        b = int(b)
        try:
            if a >= b:
                print(a / b)
            else:
                raise DivisionError(f'нельзя делить меньшее на большее: {a} на {b}')
        except DivisionError as exp:
            print('поймали ошибку:', exp)

option = input('action: ')
a = int(input('A: '))
b = int(input('B: '))
if option == '+':
    print('a + b =', a + b)
elif option == '-':
    print('a - b =', a - b)
elif option == '*':
    print('a * b =', a * b)
elif option == ':':
    print('a : b =', a / b)
else:
    print('false action')
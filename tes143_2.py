act = input('action: ')
flag = (act == '+') + (act == '-') + (act == ':') + (act == '*')
while flag == False :
    print('wrong action')
    act = input('action: ')
    flag = (act == '+') + (act == '-') + (act == ':') + (act == '*')
a = int(input('A: '))
b = int(input('B: '))
if  act == '+':
    print('a + b =', a + b)
elif act == '-':
    print('a - b =', a - b)
elif act == '*':
    print('a * b =', a * b)
elif act == ':':
    print('a : b =', a / b)
act = input('action: ')
flag = (act == '+') + (act == '-') + (act == ':') + (act == '*')
while flag == False :
    print('wrong action')
    act = input('action: ')
    flag = (act == '+') + (act == '-') + (act == ':') + (act == '*')
number_numbers = int(input('number of numbers: '))
result = int(input('number: '))
for n in range(number_numbers - 1):
    a = int(input('number: '))
    if  act == '+':
        result += a
    elif act == '-':
        result -= a
    elif act == '*':
        result *= a
    elif act == ':':
        result /= a
print(result)
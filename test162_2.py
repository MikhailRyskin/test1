number_staff = int(input('Кол-во сотрудников: '))
staff_salary = []
for staff in range(number_staff):
    print('Зарплата', staff + 1, 'сотрудника:', end='')
    salary = int(input())
    staff_salary.append(salary)
i_sal = 0
while i_sal < len(staff_salary):
    if staff_salary[i_sal] == 0:
        staff_salary.remove(staff_salary[i_sal])
        i_sal -= 1
    else:
        i_sal += 1
print('Осталось сотрудников:', len(staff_salary))
print('Зарплаты:', staff_salary)
print('Минимальная зарплата:', min(staff_salary), '\nМаксимальная зарплата:', max(staff_salary))

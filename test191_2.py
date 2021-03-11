student_str = input('Введите информацию о студенте\n'
                    '(фамилия, имя, город, вуз, оценки): ')
student_list = student_str.split()
student_dict = dict()
student_dict['Фамилия'] = student_list[0]
student_dict['Имя'] = student_list[1]
student_dict['Город'] = student_list[2]
student_dict['Вуз'] = student_list[3]
student_dict['Оценки'] = []
for i_grade in student_list[4:]:
    student_dict['Оценки'].append(i_grade)
for key in student_dict:
    print(key, student_dict[key])

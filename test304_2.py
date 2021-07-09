class Person:
    person_list = []

    # def __init__(self):
    #     pass

    def set_person(self, name, age):
        self.person_list.append({'name': name, 'age': age})


pers_1 = Person()
pers_2 = Person()
pers_3 = Person()
pers_1.set_person('John', 34)
pers_2.set_person('Paul', 23)
pers_3.set_person('Kate', 26)
print(Person.person_list)

print(sorted(Person.person_list, key= lambda elem: elem['age']))
print(sorted(Person.person_list, key= lambda elem: elem['age'], reverse=True))

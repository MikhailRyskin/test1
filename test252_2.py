class Man:

    __men_count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Man.__men_count += 1

    def get_count(self):
        return self.__men_count

    def set_name(self, name):
        if name.isalpha:
            self.__name = name
        else:
            raise Exception('имя должно быть из букв')

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            raise Exception('возраст вне диапазона')

    def get_age(self):
        return self.__age


man_1 = Man('Bob', 30)
man_2 = Man('Gtr', 40)
man_3 = Man('MMM', 50)
man_1.set_age(33)
man_2._Man__age = 44
print(man_1.get_name(), man_1.get_age(), man_2.get_name(), man_2.get_age(), man_3.get_name(), man_3.get_age())
print(man_1.get_count())

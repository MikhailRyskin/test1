from abc import abstractmethod, ABC


class Transport(ABC):
    def __init__(self, color, speed):
        self.__color = color
        self.__speed = speed

    def __str__(self):
        return f'{self.__color} {self.__speed}'

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 5 < speed < 50:
            self.__speed = speed
        else:
            raise Exception('недопустимая скорость')



    def signal(self):
        print('Bi-Bi')

    @abstractmethod
    def move(self):
        print('поехали', end=' ')


class Musicmixin():
    def music(self):
        print('ля-ля-ля')

class Auto(Transport):
    def move(self):
        super().move()
        print('по земле')


class Boat(Transport):
    def move(self):
        super().move()
        print('по воде', end=' ')


class Amfibia(Auto, Boat, Musicmixin):
    pass

amfi = Amfibia('красный', 20)
print(amfi)
amfi.move()
amfi.signal()
amfi.music()
amfi.color = 'зелёный'
amfi.speed = 60
print(amfi)


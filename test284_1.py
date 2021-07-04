from abc import abstractmethod, ABC


class Transport(ABC):
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def __str__(self):
        return f'{self.color} {self.speed}'


    def signal(self):
        print('Bi-Bi')

    @abstractmethod
    def move(self):
        print('поехали')


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
        print('по воде')


class Amfibia(Auto, Boat, Musicmixin):
    pass

amfi = Auto('красный', 20)
print(amfi)
amfi.move()
amfi.signal()
# amfi.music()


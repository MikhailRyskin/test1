class CanFly:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def take_wing(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return f'высота: {self.height}  скорость {self.speed}'


class Butterfly(CanFly):
    def take_wing(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Missile(CanFly):
    def take_wing(self):
        self.height = 500

    def fly(self):
        self.speed = 1000

    def bang(self):
        print('Ба-бах!!!')

    def land(self):
        super().land()
        self.bang()


b = Butterfly(0, 0)
r = Missile(0, 0)
print(b, r)
b.take_wing()
r.take_wing()
print(b, r)
b.fly()
r.fly()
print(b, r)
r.land()
print(b, r)

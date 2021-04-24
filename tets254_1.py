class Unit:
    def __init__(self):
        self.hit_points = 100

    def __str__(self):
        return f'хитпойнт {self.hit_points}'

    def get_damaged(self, damage):
        self.hit_points -= 0


class Solder(Unit):
    def get_damaged(self, damage):
        self.hit_points -= damage


class Sitizen(Unit):
    def get_damaged(self, damage):
        self.hit_points -= damage * 2


u = Unit()
s = Solder()
g = Sitizen()
print(u)
print(s)
print(g)
u.get_damaged(10)
s.get_damaged(10)
g.get_damaged(10)
print(u)
print(s)
print(g)

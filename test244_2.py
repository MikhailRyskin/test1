import random


class Point:

    points_count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points_count += 1

    def info(self):
        print(f'координата Х:{self.x}, координата У:{self.y}')


points = [Point(x=random.randint(0, 10), y=random.randint(0, 10)) for _ in range(15)]
for number, point in enumerate(points):
    print(f'точка {number + 1}-', end=' ')
    point.info()
print('Создано точек:', Point.points_count)

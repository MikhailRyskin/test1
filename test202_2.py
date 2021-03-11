import math


def cylinder_area(r, h):
    side = 2 * math.pi * r * h
    s = math.pi * r ** 2
    full = side + 2 * s
    return side, full


cylinder_radius = int(input('Введите радиус цилиндра: '))
cylinder_height = int(input('Введите высоту цилиндра: '))
cylinder_side, cylinder_area_full = cylinder_area(cylinder_radius, cylinder_height)
print('Площадь боковой поверхности цилиндра', cylinder_side)
print('Полная площадь цилиндра', cylinder_area_full)

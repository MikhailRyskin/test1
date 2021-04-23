class Point:

    __points_count = 0

    def __init__(self):
        self.__x = 0
        self.__y = 0
        Point.__points_count += 1

    def __str__(self):
        return f'координата Х:{self.__x}, координата У:{self.__y}'

    def set_x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x
        else:
            raise Exception('x - не число')

    def get_x(self):
        return self.__x

    def set_y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
        else:
            raise Exception('y - не число')

    def get_y(self):
        return self.__y

    def get_points_count(self):
        return self.__points_count


point_1 = Point()
point_2 = Point()
k = 788
point_1.set_y(k)
point_2.set_x(3.7)
print(point_1, point_2)
count = point_1.get_points_count()
print(count)

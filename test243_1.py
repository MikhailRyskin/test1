import random


class Toyota:

    color = 'red'
    price = 1000000
    speed = 200
    current_speed = 0

    def info(self):
        print(f'Цвет: {self.color}\nЦена:{self.price}\nТекущая скорость:{self.current_speed}')

    def get_current_speed(self, cur_speed):
        self.current_speed = cur_speed


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_2.get_current_speed(145)
car_3.current_speed = 67
car_1.info()
car_2.info()
car_3.info()

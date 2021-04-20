class Toyota:

    def __init__(self, color, price, speed, current_speed):
        self.color = color
        self.price = price
        self.speed = speed
        self.current_speed = current_speed

    def info(self):
        print(f'Цвет: {self.color}\nЦена: {self.price}\n'
              f'Максимальная скорость: {self.speed}\nТекущая скорость: {self.current_speed}')

    def get_current_speed(self, cur_speed):
        self.current_speed = cur_speed


car_1 = Toyota('red', 1200000, 210, 10)
car_2 = Toyota('blue', 1000000, 200, 50)
car_3 = Toyota('black', 900000, 160, 120)
car_1.info()
car_2.info()
car_3.info()

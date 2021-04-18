import random


class Toyota:

    color = 'red'
    price = 1000000
    speed = 200
    current_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
Toyota.current_speed = random.randint(0, 200)
print(car_1.current_speed, car_2.current_speed, car_2.current_speed)

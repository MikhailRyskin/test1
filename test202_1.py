import random


tuple_1 = tuple(random.randint(0, 5) for _ in range(10))
print(tuple_1)
tuple_2 = tuple(random.randint(-5, 0) for _ in range(10))
print(tuple_2)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
print(tuple_3.count(0))

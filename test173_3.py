import random


team_1 = [random.randint(50, 80) for _ in range(10)]
team_2 = [random.randint(30, 60) for _ in range(10)]
our_team = ['Погиб' if team_1[i] + team_2[i] > 100 else 'Выжил' for i in range(10)]
print('Урон первого отряда: ', team_1)
print('Урон второго отряда: ', team_2)
print('Состояние третьего отряда:', our_team)

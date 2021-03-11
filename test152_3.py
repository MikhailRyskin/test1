count = int(input('Введите количество собак: '))
points_list = []
for dog in range(count):
    print('Ведите очки', dog + 1, 'собаки', end=' ')
    points = int(input())
    points_list.append(points)
print('Список очков:', points_list)
maximum = points_list[0]
minimum = points_list[0]
max_ind = 0
min_ind = 0
for i in range(1, count):
    if maximum < points_list[i]:
        maximum = points_list[i]
        max_ind = i
    if minimum > points_list[i]:
        minimum = points_list[i]
        min_ind = i
print('максимум', maximum, max_ind, 'минимум', minimum, min_ind)
points_list[max_ind], points_list[min_ind] = points_list[min_ind], points_list[max_ind]
print('Исправленный список:', points_list)

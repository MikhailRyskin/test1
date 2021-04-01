import os


path = os.path.abspath(os.path.join('/', 'task', 'group_1.txt'))
print(path)
file = open(path, 'r')
summa = 0
diff = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
file.close()

path_2 = os.path.abspath(os.path.join('/', 'task', 'Additional_info', 'group_2.txt'))
print(path_2)
file_2 = open(path_2, 'r')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
file_2.close()

print(summa)
print(diff)
print(compose)

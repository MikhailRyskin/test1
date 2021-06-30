def file_lines(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            line_sum = 0
            line_list = line.split()
            for num in line_list:
                line_sum += int(num)
            yield line_sum


file_name = 'numbers.txt'
file_sum = 0
for line_sum in file_lines(file_name):
    file_sum += line_sum
print(f'Сумма чисел в файле: {file_sum}')

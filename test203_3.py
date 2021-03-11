# input_data = 'О Дивный Новый мир!'
input_data = [100, 200, 300, 'буква', 0, 2, 'а']
new_list = [data for ind, data in enumerate(input_data) if ind % 2 == 0]
print(new_list)

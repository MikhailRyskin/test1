original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_list = [(0 if x < 0 else x) for x in original_prices]
print(new_list)

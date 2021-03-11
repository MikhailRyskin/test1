incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
print(f'Общий доход за год составил {sum(incomes.values())}')
alt_dict = dict()
key_list = list(incomes.keys())
price_list = list(incomes.values())
for ind in range(len(price_list)):
    alt_dict[price_list[ind]] = key_list[ind]
min_incomes = min(price_list)
min_key = alt_dict[min_incomes]
print(f'Самый маленький доход у {min_key} Он составляет {min_incomes} рублей')
incomes.pop(min_key)
print(f'Итоговый словарь: {incomes}')

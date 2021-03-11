text = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')
double_list = [symb + symb for symb in text]
added_list = [symb + symbol for symb in double_list]
print('Список удвоенных символов:', double_list)
print('Склейка с дополнительным символом:', added_list)

def price_increase(percent, price):
    return round((price * (1 + percent / 100)), 2)


price_list = [1.09, 23.56,  57.84, 4.56, 6.78]
first = int(input('Повышение на первый год: '))
second = int(input('Повышение на второй год: '))
first_list = [price_increase(first, i_price) for i_price in price_list]
second_list = [price_increase(second, i_price) for i_price in first_list]
print('Сумма цен за каждый год:', round(sum(price_list), 2), round(sum(first_list), 2), round(sum(second_list), 2))

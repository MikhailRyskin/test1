goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент:', goods)
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))
goods.append([fruit_name, price])
print('Новый ассортимент:', goods)
for i_good in range(len(goods)):
    goods[i_good][1] = round(goods[i_good][1] * 1.08, 2)
print('Новый ассортимент с увел. ценой:', goods)

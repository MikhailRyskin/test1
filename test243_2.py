class Family:

    surname = 'Common'
    funds = 100000
    having_house = False

    def info(self):
        print(f'Фамилия {self.surname}\nНа счету {self.funds}\nЕсть дом {self.having_house}')

    def ear_money(self, money):
        self.funds += money

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.funds >= house_price:
            self.funds -= house_price
            self.having_house = True
            print('Купили дом')
        else:
            print('Не хватает денег на дом')


my_family = Family()
my_family.info()
my_family.buy_house(1000000)
my_family.ear_money(700000)
my_family.buy_house(1000000, 10)
my_family.ear_money(140000)
my_family.buy_house(1000000, 10)
my_family.info()

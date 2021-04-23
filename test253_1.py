class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'модель: {self.model}'

    def sail(self):
        print(f'корабль: {self.model} куда-то поплыл')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f'корабль: {self.model} атакует, оружие: {self.gun}')


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.load = 0

    def loading(self, cargo):
        self.load += cargo
        print(f'корабль: {self.model} загрузился, теперь количество {self.load}')

    def unloading(self, cargo):
        self.load -= cargo
        print(f'корабль: {self.model} разгрузился, теперь количество {self.load}')


varag = WarShip('крейсер', 'пушки')
print(varag)
varag.sail()
varag.attack()

barza = CargoShip('баржа')
print(barza)
barza.loading(5)
barza.unloading(2)

class Potato:

    stages = {0: 'посажена', 1: 'росток', 2: 'зелёная', 3: 'созрела'}

    def __init__(self, number):
        self.number = number
        self.stage = 0

    def info(self):
        print(f'Картошка {self.number} сейчас {Potato.stages[self.stage]}')

    def grow(self):
        if self.stage < 3:
            self.stage += 1
        self.info()

    def is_ripe(self):
        return self.stage >= 3


class PotatoGarden:

    def __init__(self, count):
        self.potato_list = [Potato(i) for i in range(1, count + 1)]

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potato_list]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')

    def grow_garden(self):
        print('Картошка прорастает!')
        for potato in self.potato_list:
            potato.grow()

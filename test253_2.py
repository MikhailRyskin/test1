class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'робот модель: {self.model}'

    def operate(self):
        print(f'робот: {self.model} действует')


class RobotVacuumCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        super().operate()
        print('собираю мусор')
        self.garbage_bag += 1


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('защищаю объект с помощью оружия:', self.gun)


class UnderwaterWarRobot(WarRobot):
    def __init__(self, model, gun, depth):
        super().__init__(model, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print('плаваю на глубине:', self.depth)


cleaner = RobotVacuumCleaner('mmm')
print(cleaner)
cleaner.operate()

war_robot = WarRobot('rr2', 'ракета')
print(war_robot)
war_robot.operate()

underwater = UnderwaterWarRobot('tt765', 'торпеда', 200)
print(underwater)
underwater.operate()

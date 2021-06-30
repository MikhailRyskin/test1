import random


class MyIterator:
    def __init__(self, number):
        self.counter = 0
        self.cur_value = round(random.randint(0, 100) / 100, 2)
        # self.cur_value = 0
        self.next_value = self.cur_value + round(random.randint(0, 100) / 100, 2)
        # self.next_value = self.cur_value + 0.6
        self.number = number

    def __iter__(self):
        # self.counter = 0
        # self.cur_value = round(random.randint(0, 100) / 100, 2)
        # self.next_value = self.cur_value + round(random.randint(0, 100) / 100, 2)
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration
            self.cur_value, self.next_value = self.next_value, self.next_value + round(random.randint(0, 100) / 100, 2)
            # self.cur_value, self.next_value = self.next_value, self.next_value + 0.6
        return round(self.cur_value, 2)


my_iterator = MyIterator(6)
for elem in my_iterator:
    print(elem)

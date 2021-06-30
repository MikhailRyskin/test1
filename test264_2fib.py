class FibIterator:
    def __init__(self, number):
        self.counter = 0
        self.cur_value = 0
        self.next_value = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.cur_value = 0
        self.next_value = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration
            self.cur_value, self.next_value = self.next_value, self.cur_value + self.next_value
        return self.cur_value


fib_iterator = FibIterator(10)
for elem in fib_iterator:
    print(elem)
print(8 in fib_iterator)

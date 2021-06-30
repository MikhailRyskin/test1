class Primes:
    def __init__(self, n):
        self.end = n
        self.start = 0
        self.prime_numbers = []

    def __iter__(self):
        self.start = 1
        self.prime_numbers = []
        return self

    def __next__(self):
        while True:
            self.start += 1
            if self.start > self.end:
                raise StopIteration()
            else:
                for prime in self.prime_numbers:
                    if self.start % prime == 0:
                        break
                else:
                    self.prime_numbers.append(self.start)
                    return self.start


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
print(41 in prime_nums)

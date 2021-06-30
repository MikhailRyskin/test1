class CountIterator:
    def __init__(self):
        self.__counter = 0

    def __str__(self):
        return self.__counter

    def __iter__(self):
        return self

    def __next__(self):
        self.__counter += 1
        return self.__counter


my_iter = CountIterator()

for i_elem in my_iter:
    print(i_elem)

my_list = [10, 20, 30, 40, 50]
# my_iterator = iter(my_list)
my_iterator = my_list.__iter__()
while True:
    try:
        # next_elem = next(my_iterator)
        next_elem = my_iterator.__next__()
        print(next_elem)
    except StopIteration:
        break

from functools import reduce

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic",
             "because his mother was a Catholic", "or had been"]


# def func_1(str_1, str_2):
#     res = str_1 + ' ' + str_2
#     return res


print(reduce(lambda x, y: x + ' ' + y, sentences).count('was'))

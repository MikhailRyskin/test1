import random


def change_dict(dct):

    num = random.randint(1, 100)
    print(num)

    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            new_list = i_value + [num]
            dct[i_key] = new_list
        elif isinstance(i_value, dict):
            new_dict = {num: 'случайный текст'}
            new_dict.update(i_value)
            dct[i_key] = new_dict
        elif isinstance(i_value, set):
            new_set = i_value | {num}
            dct[i_key] = new_set
        elif isinstance(i_value, tuple):
            new_tuple = list(i_value)
            new_tuple.append(num)
            dct[i_key] = tuple(new_tuple)


nums_list = [1, 2, 3]

some_dict = {1: 'text', 2: 'another text'}

uniq_nums = {1, 2, 3}

common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}


change_dict(common_dict)

print(common_dict)
print(nums_list, some_dict, uniq_nums)

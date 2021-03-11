def create_dict(data):
    if isinstance(data, dict):
        return data
    elif isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template = dict()
        template[data] = data
        return template
    # else:
    #     return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        if create_dict(i_element):
            new_list.append(create_dict(i_element))
    return new_list


data = ['sad', {'sds': 23}, {43}, 67.98, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)

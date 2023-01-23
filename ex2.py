def combine_dicts(dict1, dict2):
    return {key: dict1[key] + dict2[key] for key in dict1 if key in dict2}
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = combine_dicts(my_dict_1, my_dict_2)
print(combined_dict)
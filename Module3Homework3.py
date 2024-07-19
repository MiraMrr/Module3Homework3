def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(a = 2, b = False)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1.5, 8, 'word']
values_dict = {'a': 4, 'b': 25.5, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 10]

print_params(*values_list_2, 42)

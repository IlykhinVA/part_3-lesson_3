values_list = [True, 'проба', 56]
values_dict = {'a': 'Петя', 'b': 'рыжий', 'c': 'худой'}
values_list_2 = [54.32, 'опять строчка']


def print_params(a=1, b='строчка', c=True):
    return (a, b, c)


print(*print_params())
print(*print_params(7, 'еще строка', False))
print(*print_params(47, True))
print(*print_params(c=99))
print(*print_params(b=25, c=[1, 2, 3]))
print(*print_params(*values_list))
print(*print_params(**values_dict))
print(print_params(*values_list_2, 49))

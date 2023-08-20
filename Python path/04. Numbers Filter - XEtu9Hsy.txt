def even_odd_filter(**kwargs):
    new_dict = {}

    for name, value in kwargs.items():

        if name not in new_dict:
            new_dict[name] = {}

        if name != 'odd':
            even = list(filter(lambda n: n % 2 == 0, value))
            new_dict[name] = even
        else:
            odd = list(filter(lambda x: x % 2 != 0, value))
            new_dict[name] = odd

    new_dict = sorted(new_dict.items(), key=lambda x: -len(x[1]))
    return dict(new_dict)


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
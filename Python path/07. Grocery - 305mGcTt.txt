def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    kwargs = dict(kwargs)
    return "\n".join([(f'{key}: {value}') for key, value in kwargs.items()])


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

def math_operations(*args, **kwargs):
    count = 1

    for x in args:
        if count == 1:
            kwargs['a'] += x
        elif count == 2:
            kwargs['s'] -= x
        elif count == 3:
            if x == 0 or kwargs['d'] == 0:
                count += 1
                continue
            else:
                kwargs['d'] /= x
        elif count == 4:
            kwargs['m'] *= x

        count += 1
        if count > 4:
            count = 1

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    new = dict(kwargs)

    return "\n".join([f'{key}: {value:.1f}' for key, value in new.items()])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print()
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print()
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


def func_executor(*args):
    final = []
    for x in args:
        name = x[0].__name__
        result = x[0](*x[1])

        final.append(f"{name} - {result}")

    return '\n'.join(final)

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

print(func_executor((make_upper, ("Python", "softUni")),(make_lower, ("PyThOn",)),))
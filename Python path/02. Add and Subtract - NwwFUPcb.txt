def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num3):
    return num3


number1 = int(input())
number2 = int(input())
number3 = int(input())


def final(a, b, c):
    return sum_numbers(number1, number2) - subtract(number3)


print(final(number1, number2, number3))

n = int(input())


even = list()
odd = list()
negative = list()
positive = list()


for i in range(n):
    numbers = int(input())

    if numbers % 2 == 0:
        even.append(numbers)
    else:
        odd.append(numbers)

    if numbers >= 0:
        positive.append(numbers)
    else:
        negative.append(numbers)

command = input()

print(eval(command))
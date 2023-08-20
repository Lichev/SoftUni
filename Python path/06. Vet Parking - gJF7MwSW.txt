import math

days = int(input())
hours = int(input())

parking = 0

for i in range(1, days + 1):
    temp = 0

    for k in range(1, hours + 1):
        if i % 2 == 0 and k % 2 != 0:
            parking += 2.50
            temp += 2.5
        elif i % 2 != 0 and k % 2 == 0:
            parking += 1.25
            temp += 1.25
        else:
            parking += 1
            temp += 1
    print(f'Day: {i} - {temp:.2f} leva')


print(f"Total: {parking:.2f} leva")


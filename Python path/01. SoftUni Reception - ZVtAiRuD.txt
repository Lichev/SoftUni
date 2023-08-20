one = int(input())
two = int(input())
three = int(input())
students = int(input())

per_hours = one + two + three
hours = 0

while students > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    students -= per_hours


print(f'Time needed: {hours}h.')
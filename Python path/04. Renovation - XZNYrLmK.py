import math

height = int(input())
width = int(input())
percent = int(input())

total = height * width * 4
all = math.ceil(total - (total * (percent / 100)))

while all >= 0:
    boq = input()

    if boq == 'Tired!':
        break

    all -= int(boq)

if all < 0:
    print(f"All walls are painted and you have {abs(all)} l paint left!")
elif all == 0:
    print(f'All walls are painted! Great job, Pesho!')
else:
    print(f"{all} quadratic m left.")

width = int(input())
length = int(input())
height = int(input())

all = width * length * height
needed = 0

while all > needed:
    broi = input()

    if broi == 'Done':
        break

    k = int(broi)
    needed += k


result = abs(all - needed)

if all >= needed:
    print(f"{result} Cubic meters left.")
else:
    print(f"No more free space! You need {result} Cubic meters more.")
n = int(input())

all = 255
sum = 0

for i in range(n):
    water = int(input())

    if (sum + water) > all:
        print(f'Insufficient capacity!')
        continue

    sum += water

print(sum)
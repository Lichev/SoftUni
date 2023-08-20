bought_food = int(input())

grams = bought_food * 1000
count = 0

while True:
    ate = input()

    if ate == 'Adopted':
        break

    count += int(ate)

diff = abs(grams - count)

if grams >= count:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
group_size = int(input())
days = int(input())

coins = 0

motivational = False

for i in range(1, days + 1):

    if i % 10 == 0:
        group_size -= 2

    if i % 15 == 0:
        group_size += 5

    coins += 50
    coins -= (group_size * 2)

    if i % 3 == 0:
        coins -= group_size * 3
        motivational = True

    if i % 5 == 0:
        coins += group_size * 20
        if motivational:
            coins -= group_size * 2

    motivational = False

print(f'{group_size} companions received {int(coins/group_size)} coins each.')

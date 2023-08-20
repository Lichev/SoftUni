def fire(index, damage, warship):
    validation = 0 <= index < len(warship)
    if validation:
        warship[index] -= damage
        if warship[index] < 0:
            warship[index] = 0
    return warship


def defend(start, end, damage, my_ships):
    validation = start >= 0 and end < len(my_ships)
    if validation:
        for i in range(start, end + 1):
            my_ships[i] -= damage
            if my_ships[i] < 0:
                my_ships[i] = 0
    return my_ships


def repair(index, health, max_health, myship):
    validation = 0 <= index < len(myship)
    if validation:
        if myship[index] + health > max_health:
            myship[index] = max_health
        else:
            myship[index] += health

    return myship


def status(max, myship):
    count = 0
    min = max * 0.20
    for i in myship:
        if i < min:
            count += 1

    return count


def general(myship, warship, max):
    win_lose = True

    while True:
        command = input()

        if command == 'Retire':
            break

        command = command.split(" ")
        action = command[0]

        if action == 'Fire':
            index = int(command[1])
            damage = int(command[2])
            warship = fire(index, damage, warship)
            if 0 in warship:
                print(f'You won! The enemy ship has sunken.')
                win_lose = False
                break
        elif action == 'Defend':
            start_index = int(command[1])
            end_index = int(command[2])
            damage = int(command[3])
            myship = defend(start_index, end_index, damage, myship)
            if 0 in myship:
                print(f'You lost! The pirate ship has sunken.')
                win_lose = False
                break
        elif action == 'Repair':
            index = int(command[1])
            health = int(command[2])
            myship = repair(index, health, max, myship)

        elif action == 'Status':
            needed_repair = status(max, myship)
            print(f'{needed_repair} sections need repair.')

    if win_lose:
        print(f'Pirate ship status: {sum(myship)}')
        print(f'Warship status: {sum(warship)}')


my_ship = [int(i) for i in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())
general(my_ship, warship, max_health)

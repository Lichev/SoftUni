def list_of_loots(items):
    new_list = []
    for i in range(1, len(items)):
        new_list.append(items[i])
    return new_list


def loot(looted, items):
    for i in looted:
        if i not in items:
            items.insert(0, i)
    return items


def drop(index, treasures):
    valid = 0 <= index < len(treasures)
    if valid:
        treasures.append(treasures[index])
        treasures.pop(index)
    return treasures


def steal(count, treasures):
    new_list = []
    current_count = 1
    if count > len(treasures):
        count = len(treasures)
    for i in range(count):
        new_list.append(treasures[-current_count])

        current_count += 1

    print(", ".join(reversed(new_list)))
    treasures = [i for i in treasures if i not in new_list]
    return treasures


def average_treasure(treasure):
    count = 0

    for i in treasure:
        count += len(i)

    averege = count / len(treasure)
    return averege


def general(treasures):
    while True:
        commands = input()

        if commands == 'Yohoho!':
            break

        commands = commands.split(" ")
        action = commands[0]

        if action == 'Loot':
            list_of_items = list_of_loots(commands)
            treasures = loot(list_of_items, treasures)
        elif action == 'Drop':
            index = int(commands[1])
            treasures = drop(index, treasures)
        elif action == 'Steal':
            count = int(commands[1])
            treasures = steal(count, treasures)

    if len(treasures) != 0:
        averageGain = average_treasure(treasures)
        print(f'Average treasure gain: {averageGain:.2f} pirate credits.')
    else:
        print(f'Failed treasure hunt.')


initial_treasure = input().split("|")
general(initial_treasure)

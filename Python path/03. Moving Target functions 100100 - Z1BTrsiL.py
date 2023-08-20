def shoot(index, power, targets):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print(f'Invalid placement!')
    return targets


def strike(index, radius, targets):
    start_index = index - radius
    end_index = index + radius
    validation = start_index >= 0 and end_index < len(targets)

    if validation:
        targets = [targets[i] for i in range(len(targets)) if i < start_index or i > end_index]
    else:
        print(f'Strike missed!')

    return targets


def general(targets):
    while True:
        command = input()

        if command == 'End':
            print("|".join(map(str, targets)))
            break

        command = command.split(" ")

        action = command[0]
        index = int(command[1])
        value = int(command[2])

        if action == 'Shoot':
            targets = shoot(index, value, targets)
        elif action == 'Add':
            targets = add(index, value, targets)
        elif action == 'Strike':
            targets = strike(index, value, targets)



data = list(map(int, input().split(" ")))
general(data)


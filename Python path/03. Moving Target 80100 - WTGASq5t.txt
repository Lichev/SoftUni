targets = [int(n) for n in input().split(" ")]

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(" ")
    action = data[0]
    index = int(data[1])
    value = int(data[2])

    if action == 'Shoot':
        if index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                del targets[index]
    elif action == 'Add':
        if index < len(targets):
            targets.insert(index, value)
        else:
            print(f'Invalid placement!')
    elif action == 'Strike':
        sum1 = index + value
        sum2 = index - value

        lst = []

        if index + value < len(targets) and index - value >= 0:
            for i in range(index, sum1 + 1):
                lst.append(targets[i])
            for n in range(index - 1, sum2 - 1, -1):
                lst.append(targets[n])
        else:
            print(f'Strike missed!')
        targets = [int(x) for x in targets if x not in lst]

mapping = list(map(str, targets))
print(*mapping, sep="|")
targets = [int(x) for x in input().split(" ")]

count = 0

while True:
    command = input()

    if command == 'End':
        break

    data = int(command)

    if data < len(targets):
        current_target = int(targets[data])
        if targets[data] != -1:
            targets[data] = -1
            count += 1

        for current in range(len(targets)):
            if targets[current] == -1:
                continue
            if current_target >= targets[current]:
                targets[current] += current_target
            else:
                targets[current] -= current_target

to_str = list(map(str, targets))

print(f'Shot targets: {count} -> {" ".join(to_str)}')
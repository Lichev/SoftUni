numbers = [int(n) for n in input().split(" ")]

while True:
    command = input()

    if command == 'end':
        break

    data = command.split(" ")
    action = data[0]

    if action != 'decrease':
        index1 = int(data[1])
        index2 = int(data[2])

    if action == 'swap':
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == 'multiply':
        numbers[index1] = numbers[index1] * numbers[index2]
    elif action == 'decrease':
        for x, n in enumerate(numbers):
            numbers[x] -= 1

print(", ".join(map(str, numbers)))

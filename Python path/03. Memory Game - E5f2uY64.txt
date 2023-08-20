elements = [x for x in input().split(" ")]
moves = 0

while True:
    command = input()

    if command == 'end':
        break

    data = command.split(" ")
    index1 = data[0]
    index2 = data[1]

    half_index = int(len(elements) / 2)

    if int(index1) == int(index2) or int(index1) < 0 or int(index2) < 0 or int(index1) > len(elements) or int(
            index2) > (len(elements)):
        moves += 1
        new = "-" + str(moves) + "a"

        elements.insert(half_index, new)
        elements.insert(half_index + 1, new)

        print(f"Invalid input! Adding additional elements to the board")

    elif elements[int(index1)] == elements[int(index2)]:
        print(f'Congrats! You have found matching elements - {elements[int(index1)]}!')
        new_list = [int(index1), int(index2)]

        elements = [i for j, i in enumerate(elements) if j not in new_list]

        moves += 1
    elif elements[int(index1)] != elements[int(index2)]:
        print(f'Try again!')
        moves += 1

    if len(elements) == 0:
        print(f'You have won in {moves} turns!')
        break

if len(elements) != 0:
    print(f'Sorry you lose :(')
    print(*elements, sep=" ")

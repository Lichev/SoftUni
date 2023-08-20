from collections import deque

order_of_turns = deque(input().split(", "))
matrix = [input().split() for x in range(6)]

penalty_name = deque()

while True:
    coordinates = input()
    row = int(coordinates[1])
    col = int(coordinates[4])
    current_el = matrix[row][col]
    current_player = order_of_turns.popleft()

    if penalty_name:
        if current_player == penalty_name[0]:
            order_of_turns.append(penalty_name.popleft())
            continue

    if matrix[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == 'T':
        print(f"{current_player} is out of the game! The winner is {order_of_turns[0]}." )
        break
    elif matrix[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        penalty_name.append(current_player)

    order_of_turns.append(current_player)
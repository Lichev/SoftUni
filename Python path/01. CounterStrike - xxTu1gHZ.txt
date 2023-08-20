energy = int(input())

wins = 0

while energy >= 0:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break

    data = int(command)

    if energy - data >= 0:
        energy -= data
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break

    if wins % 3 == 0:
        energy += wins
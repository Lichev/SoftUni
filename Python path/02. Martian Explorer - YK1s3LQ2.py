from collections import deque

matrix = []

rover_row = 0
rover_cow = 0

for r in range(6):
    data = list(input().split())
    matrix.append(data)
    for c in range(len(data)):
        if data[c] == 'E':
            rover_row = r
            rover_cow = c

commands = deque(input().split(", "))

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
broken = False

while True:
    if broken:
        print(f"Rover got broken at ({rover_row}, {rover_cow})")

    if not commands:
        break

    current_command = commands.popleft()

    if current_command == 'up':
        rover_row -= 1
        if rover_row < 0:
            rover_row = 5

    elif current_command == 'down':
        rover_row += 1
        if rover_row > 5:
            rover_row = 0

    elif current_command == 'right':
        rover_cow += 1
        if rover_cow > 5:
            rover_cow = 0

    elif current_command == 'left':
        rover_cow -= 1
        if rover_cow < 0:
            rover_cow = 5

    if matrix[rover_row][rover_cow] == "W":
        print(f'Water deposit found at ({rover_row}, {rover_cow})')
        water_deposit += 1
        matrix[rover_row][rover_cow] = 'E'

    elif matrix[rover_row][rover_cow] == "M":
        metal_deposit += 1
        matrix[rover_row][rover_cow] = 'E'
        print(f"Metal deposit found at ({rover_row}, {rover_cow})")

    elif matrix[rover_row][rover_cow] == "C":
        print(f"Concrete deposit found at ({rover_row}, {rover_cow})")
        concrete_deposit += 1
        matrix[rover_row][rover_cow] = 'E'

    elif matrix[rover_row][rover_cow] == "R":
        broken = True


if metal_deposit > 0 and water_deposit > 0 and concrete_deposit > 0:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
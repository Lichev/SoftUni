player_name = input()

starting_points = 301
succes = 0
unsucces = 0

while True:
    pole = input()

    if pole == 'Retire':
        print(f"{player_name} retired after {unsucces} unsuccessful shots.")
        break

    points = int(input())

    if pole == 'Single':
        points = points
    elif pole == 'Double':
        points = points * 2
    elif pole == 'Triple':
        points = points * 3

    if starting_points >= points:
        starting_points -= points
        succes += 1
    elif points > starting_points:
        unsucces += 1

    if starting_points == 0:
        print(f"{player_name} won the leg with {succes} shots.")
        break

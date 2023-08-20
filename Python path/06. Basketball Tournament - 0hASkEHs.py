wins = 0
lose = 0
total = 0

while True:
    name = input()
    if name == "End of tournaments":
        print(f"{(wins / total) * 100:.2f}% matches win")
        print(f"{(lose / total) * 100:.2f}% matches lost")
        break

    number_of_games = int(input())

    for i in range(1, number_of_games + 1):
        desi_points = int(input())
        others_points = int(input())

        diff = abs(desi_points - others_points)

        if desi_points > others_points:
            print(f'Game {i} of tournament {name}: win with {diff} points.')
            wins += 1
            total += 1
        else:
            print(f"Game {i} of tournament {name}: lost with {diff} points.")
            lose += 1
            total += 1

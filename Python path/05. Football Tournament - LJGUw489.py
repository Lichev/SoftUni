team_name = input()
played = int(input())

points = 0
w = 0
d = 0
l = 0

for i in range(played):
    results_from_games = input()

    if results_from_games == 'W':
        w += 1
        points += 3
    elif results_from_games == 'D':
        d += 1
        points += 1
    elif results_from_games == 'L':
        l += 1

if played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f'{team_name} has won {points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {l}')
    print(f'Win rate: {(w / played) * 100:.2f}%')

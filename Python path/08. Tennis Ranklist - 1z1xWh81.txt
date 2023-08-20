import math
number_of_tournaments = int(input())
starting_score = int(input())

scores = starting_score
wins = 0
for i in range(number_of_tournaments):
    etap = input()

    if etap == 'W':
        scores += 2000
        wins += 1
    elif etap == 'F':
        scores += 1200
    elif etap == 'SF':
        scores += 720

avarage = (scores - starting_score) / number_of_tournaments
percent_of_wins = (wins / number_of_tournaments) * 100

print(f'Final points: {scores}')
print(f'Average points: {math.floor(avarage)}')
print(f'{percent_of_wins:.2f}%')
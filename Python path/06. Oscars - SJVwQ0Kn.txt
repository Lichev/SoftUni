name_of_actor = input()
score_from_academy = float(input())
n_of_judges = int(input())

total = score_from_academy

for i in range(n_of_judges):
    name_of_judge = input()
    score_judge = float(input())

    length = len(name_of_judge)

    if total < 1250.5:
        total = total + ((length * score_judge) / 2)

diff = abs(1250.5 - total)
if total > 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total:.1f}!')
else:
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')
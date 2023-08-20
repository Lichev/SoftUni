budget = float(input())
fuel_need = float(input())
day_of_week = input()

fuel_money = fuel_need * 2.10
all = fuel_money + 100


if day_of_week == 'Saturday':
    all = all - (all * 0.10)
elif day_of_week == 'Sunday':
    all = all - (all * 0.20)

diff = abs(budget - all)

if budget >= all:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')
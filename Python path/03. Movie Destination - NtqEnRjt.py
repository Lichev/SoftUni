budget_film = float(input())
destination = input()
season = input()
days_to_stay = int(input())

result = 0

if destination == 'Dubai':
    if season == 'Winter':
        result = days_to_stay * 45000
    else:
        result = days_to_stay * 40000
    result = result - (result * 0.30)
elif destination == 'Sofia':
    if season == 'Winter':
        result = days_to_stay * 17000
    else:
        result = days_to_stay * 12500
    result = result + (result * 0.25)
elif destination == 'London':
    if season == 'Winter':
        result = days_to_stay * 24000
    else:
        result = days_to_stay * 20250


diff = abs(result - budget_film)

if budget_film >= result:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')
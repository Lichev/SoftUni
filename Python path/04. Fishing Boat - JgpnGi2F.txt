budget = int(input())
season = input()
number_of_people = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
    if number_of_people <= 6:
        rent -= rent * 0.10
    elif 7 < number_of_people <= 11:
        rent -= rent * 0.15
    elif number_of_people > 12:
        rent -= rent * 0.25
elif season == 'Summer':
    rent = 4200
    if number_of_people <= 6:
        rent -= rent * 0.10
    elif 7 < number_of_people <= 11:
        rent -= rent * 0.15
    elif number_of_people > 12:
        rent -= rent * 0.25
elif season == 'Autumn':
    rent = 4200
    if number_of_people <= 6:
        rent -= rent * 0.10
    elif 7 < number_of_people <= 11:
        rent -= rent * 0.15
    elif number_of_people > 12:
        rent -= rent * 0.25
elif season == 'Winter':
    rent = 2600
    if number_of_people <= 6:
        rent -= rent * 0.10
    elif 7 < number_of_people <= 11:
        rent -= rent * 0.15
    elif number_of_people > 12:
        rent -= rent * 0.25

if (number_of_people % 2) == 0 and season != 'Autumn':
    rent -= rent * 0.05

diff = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

city_name = input()
package = input()
yes_or_no = input()
residence = int(input())

per_night = 0
money = 0

if city_name == 'Bansko' or city_name == 'Borovets':
    if package == 'noEquipment':
        per_night += 80
        if yes_or_no == 'yes':
            per_night = per_night - (per_night * 0.05)
    elif package == 'withEquipment':
        per_night += 100
        if yes_or_no == 'yes':
            per_night = per_night - (per_night * 0.10)
    else:
        print('Invalid input!')
elif city_name == 'Varna' or city_name == 'Burgas':
    if package == 'noBreakfast':
        per_night += 100
        if yes_or_no == 'yes':
            per_night = per_night - (per_night * 0.07)
    elif package == 'withBreakfast':
        per_night += 130
        if yes_or_no == 'yes':
            per_night = per_night - (per_night * 0.12)
    else:
        print('Invalid input!')
else:
    print('Invalid input!')

if residence > 7:
    money = (residence - 1) * per_night
else:
    money = residence * per_night

if residence != 0 and money != 0:
    print(f'The price is {money:.2f}lv! Have a nice time!')
elif residence == 0:
    print('Days must be positive number!')

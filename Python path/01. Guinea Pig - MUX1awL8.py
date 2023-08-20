quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
pig_weight = float(input())

food_gr = quantity_food * 1000
hay_gr = quantity_hay * 1000
cover_gr = quantity_cover * 1000
pig_gr = pig_weight * 1000

days = 0

while days <= 29:
    if food_gr > 0 and hay_gr > 0 and cover_gr > 0:
        food_gr -= 300
        days += 1
        if days % 2 == 0:
            hay_gr -= food_gr * 0.05
        if days % 3 == 0:
            cover_gr -= pig_gr / 3

    else:
        break

if food_gr > 0 and hay_gr > 0 and cover_gr > 0:
    print(
        f'Everything is fine! Puppy is happy! Food: '
        f'{food_gr / 1000:.2f}, Hay: {hay_gr / 1000:.2f}, Cover: {cover_gr / 1000:.2f}.')
else:
    print(f'Merry must go to the pet store!')

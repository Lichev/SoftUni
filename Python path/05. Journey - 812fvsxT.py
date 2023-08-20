budget = float(input())
season = input()

result = 0
where = ''
what = ''

if budget <= 100:
    if season == 'summer':
        result = budget * 0.30
        where = 'Bulgaria'
        what = 'Camp'
    elif season == 'winter':
        result = budget * 0.70
        where = 'Bulgaria'
        what = 'Hotel'
elif 101 <= budget <= 1000:
    if season == 'summer':
        result = budget * 0.40
        where = 'Balkans'
        what = 'Camp'
    elif season == 'winter':
        result = budget * 0.80
        where = 'Balkans'
        what = 'Hotel'
elif budget  > 1000:
    if season == 'summer':
        result = budget * 0.90
        where = 'Europe'
        what = 'Hotel'
    elif season == 'winter':
        result = budget * 0.90
        where = 'Europe'
        what = 'Hotel'

print(f'Somewhere in {where}')
print(f'{what} - {result:.2f}')

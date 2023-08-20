month = input()
nights = int(input())

price = 0
studio = 0
apart = 0

if month == 'May' or month == 'October':
    studio = 50
    apart = 65
    if nights > 7 and nights <= 13:
        studio = studio - (studio * 0.05)
    elif nights > 14:
        studio = studio - (studio * 0.30)
        apart = apart - (apart * 0.10)
elif month == 'June' or month == 'September':
    studio = 75.20
    apart = 68.70
    if nights > 14:
        studio = studio - (studio * 0.20)
        apart = apart - (apart * 0.10)
elif month == 'July' or month == 'August':
    studio = 76
    apart = 77
    if nights > 14:
        apart = apart - (apart * 0.10)

resultS = studio * nights
resultA = apart * nights
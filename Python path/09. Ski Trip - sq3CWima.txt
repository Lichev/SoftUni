days = int(input())
type_of_room = input()
rating = input()

nights = days - 1
price = 0

if type_of_room == 'room for one person':
    price = nights * 18
elif type_of_room == 'apartment':
    price = nights * 25
    if days < 10:
        price = price - (price * 0.30)
    elif 10 < days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.50)
elif type_of_room == 'president apartment':
    price = nights * 35
    if days < 10:
        price = price - (price * 0.30)
    elif 10 < days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.20)

if rating == 'positive':
    price = price + (price * 0.25)
elif rating == 'negative':
    price = price - (price * 0.10)

print(f'{price:.2f}')
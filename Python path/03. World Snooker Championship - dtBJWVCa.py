stage = input()
ticket_type = input()
number_tickets = int(input())
pictures = input()

price = 0

if ticket_type == 'Standard':
    if stage == 'Quarter final':
        price = 55.50
    elif stage == 'Semi final':
        price = 75.88
    elif stage == 'Final':
        price = 110.10
elif ticket_type == "Premium":
    if stage == 'Quarter final':
        price = 105.20
    elif stage == 'Semi final':
        price = 125.22
    elif stage == 'Final':
        price = 160.66
elif ticket_type == 'VIP':
    if stage == 'Quarter final':
        price = 118.90
    elif stage == 'Semi final':
        price = 300.40
    elif stage == 'Final':
        price = 400

total = number_tickets * price


trofei = 0
if pictures == "Y":
    trofei = 40 * number_tickets

if total > 4000:
    total = total - (total * 0.25)
elif 2500 < total <= 4000:
    total = total - (total * 0.10) + trofei
else:
    total = total + trofei

print(f'{total:.2f}')


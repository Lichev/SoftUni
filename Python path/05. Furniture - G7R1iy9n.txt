import re

command = input()

forniture_list = []
total_price = 0

while command != 'Purchase':
    rex = r'>>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+[\.*0-9]+)!(?P<quantity>[0-9]+)\b'
    matches = re.finditer(rex, command)
    for match in matches:
        furniture = match.group('furniture')
        price = match.group('price')
        quantity = match.group('quantity')

        forniture_list.append(furniture)

        total_price += float(price) * float(quantity)

    command = input()


print(f'Bought furniture:')
for forni in forniture_list:
    print(forni)
print(f'Total money spend: {total_price:.2f}')

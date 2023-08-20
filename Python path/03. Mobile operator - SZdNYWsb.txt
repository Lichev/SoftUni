contract_time = input()
type_of_contract = input()
internet = input()
months = int(input())

price = 0

if contract_time == 'one':
    if type_of_contract == 'Small':
        price = 9.98
    elif type_of_contract == 'Middle':
        price = 18.99
    elif type_of_contract == 'Large':
        price = 25.98
    elif type_of_contract == 'ExtraLarge':
        price = 35.99
elif contract_time == 'two':
    if type_of_contract == 'Small':
        price = 8.58
    elif type_of_contract == 'Middle':
        price = 17.09
    elif type_of_contract == 'Large':
        price = 23.59
    elif type_of_contract == 'ExtraLarge':
        price = 31.79

if internet == 'yes':
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_time == 'two':
    price = price - (price * 0.0375)

print(f"{months*price:.2f} lv.")

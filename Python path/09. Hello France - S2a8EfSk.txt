items = input().split("|")
budget = float(input())

start = budget
price = 0
list_of_price = list()
for current in items:
    my_list = current.split('->')
    type_item = my_list[0]
    max_price = float(my_list[1])

    is_legit = False

    if type_item == 'Clothes' and 0 <= max_price <= 50.00:
        is_legit = True
    elif type_item == 'Shoes' and 0 <= max_price <= 35.00:
        is_legit = True
    elif type_item == 'Accessories' and 0 <= max_price <= 20.50:
        is_legit = True

    if is_legit and start >= max_price:
        start -= max_price
        price += max_price + (max_price * 0.40)
        max_price = max_price + (max_price * 0.40)
        list_of_price.append("%.2f"%max_price)

    else:
        continue

print(*list_of_price, sep=' ')
print(f'Profit: {price - budget + start:.2f}')

if price + start > 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')

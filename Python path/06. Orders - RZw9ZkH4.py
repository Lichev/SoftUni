from collections import defaultdict

command = input()
my_dict = {}
prices = {}
while command != 'buy':
    data = command.split(" ")
    product = data[0]
    price = float(data[1])
    quantity = float(data[2])

    if product not in my_dict:
        my_dict[product] = 0
        prices[product] = 0
    my_dict[product] += quantity
    prices[product] = price

    command = input()


for quantity_key, quantity_value in my_dict.items():
    for price_key, price_value in prices.items():
        if quantity_key == price_key:
            print(f"{quantity_key} -> {quantity_value * price_value:.2f}")
            break
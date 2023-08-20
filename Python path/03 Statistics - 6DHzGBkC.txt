products = {}

while True:
    commands = input()

    if commands == "statistics":
        break

    data = commands.split(": ")
    current_product = data[0]
    current_value = int(data[1])

    if current_product not in products:
        products[current_product] = current_value
    else:
        products[current_product] += current_value

print(f'Products in stock:')
for key, value in products.items():
    print(f"- {key}: {value}")

print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
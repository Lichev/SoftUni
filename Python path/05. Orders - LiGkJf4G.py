number_of_orders = int(input())

results = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())

    if 0 < price_per_capsule <= 100.00 and 0 < days <= 31 and 0 < caps_per_day <= 2000:
        result_per_day = price_per_capsule * caps_per_day * days
        results += result_per_day
        print(f'The price for the coffee is: ${result_per_day:.2f}')
    else:
        continue

print(f'Total: ${results:.2f}')

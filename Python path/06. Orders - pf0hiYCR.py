orders = int(input())

total = 0

for i in range(orders):
    price_for_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    per_order = price_for_capsule * days * capsules_count
    total += per_order

    print(f"The price for the coffee is: ${per_order:.2f}")
print(f"Total: ${total:.2f}")



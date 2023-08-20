budget = int(input())

while True:
    price = input()

    if price == 'End':
        print(f'You bought everything needed.')
        break

    if budget - int(price) < 0:
        print(f"You went in overdraft!")
        break

    budget -= int(price)

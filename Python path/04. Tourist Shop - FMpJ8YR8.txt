budget = float(input())

money = budget
count = 0
spent = 0

while money >= 0:
    product_name = input()

    if product_name == 'Stop':
        print(f"You bought {count} products for {spent:.2f} leva.")
        break

    product_price = float(input())
    count += 1
    if count % 3 == 0:
        product_price = product_price / 2

    money -= product_price
    spent += product_price

if money < 0:
    print(f"You don't have enough money!")
    print(f"You need {abs(money):.2f} leva!")


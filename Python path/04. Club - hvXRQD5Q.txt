needed_money = float(input())

gathered_money = 0
length = 0

while needed_money > gathered_money:
    cocktail = input()
    if cocktail == "Party!":
        break
    length = len(cocktail)

    temporary = 0

    number_of_cocktails = int(input())
    temporary = length * number_of_cocktails

    if temporary % 2 != 0:
        temporary = temporary - (temporary * 0.25)

    gathered_money += temporary

diff = abs(needed_money - gathered_money)
if needed_money > gathered_money:
    print(f"We need {diff:.2f} leva more.")
else:
    print(f"Target acquired.")

print(f"Club income - {gathered_money:.2f} leva.")
price_for_20 = float(input())
kg_of_bag = float(input())
days_on_road = int(input())
number_of_bags = int(input())

sums = 0

if kg_of_bag < 10:
    sums = price_for_20 * 0.20
elif 10 <= kg_of_bag <= 20:
    sums = price_for_20 * 0.50
elif kg_of_bag > 20:
    sums = price_for_20

if days_on_road > 30:
    sums = sums + (sums * 0.10)
elif 7 <= days_on_road <= 30:
    sums = sums + (sums * 0.15)
else:
    sums = sums + (sums * 0.40)

final = number_of_bags * sums

print(f"The total price of bags is: {final:.2f} lv. ")
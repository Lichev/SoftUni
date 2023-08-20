from math import floor

age = int(input())
wash_machine = float(input())
price_for_toy = int(input())

money_even = 0
toys_odd = 0


for t in range(1, age + 1):
    if t % 2 == 0:
        money_even += 10 * (t / 2)

    else:
        toys_odd += 1


money_for_toys = toys_odd * price_for_toy
brother_money = floor(age/2)
all_money = money_for_toys + money_even - brother_money

diff = abs(all_money - wash_machine)

if wash_machine < all_money:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')


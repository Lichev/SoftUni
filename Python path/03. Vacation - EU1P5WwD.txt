needed_money = float(input())
available_money = float(input())

spend_counter = 0
all_money = available_money
days_counter = 0

while all_money < needed_money and spend_counter < 5:
    action = input()
    money = float(input())

    days_counter += 1

    if action == 'spend':
        spend_counter += 1
        all_money -= money
        if all_money < 0:
            all_money = 0
    elif action == 'save':
        all_money += money
        spend_counter = 0

if spend_counter == 5:
    print("You can't save the money.")
    print(days_counter)
if all_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')


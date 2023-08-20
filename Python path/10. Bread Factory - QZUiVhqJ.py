events = input().split('|')

energy = 100
coins = 100
impossible = True

for event in events:
    current_event = event.split('-')

    name_event = current_event[0]
    number = int(current_event[1])

    if name_event == 'rest':
        if (number + energy) > 100:
            gained = number - (energy + number - 100)
            energy = 100
            print(f"You gained {gained} energy.")
            print(f'Current energy: {energy}.')
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f'Current energy: {energy}.')
    elif name_event == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f'You earned {number} coins.')
        else:
            if (energy + 50) > 100:
                energy = 100
            else:
                energy += 50
            print(f'You had to rest!')

    else:
        coins -= number
        if coins > 0:
            print(f'You bought {name_event}.')
        else:
            print(f'Closed! Cannot afford {name_event}.')
            impossible = False
            break

if impossible:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

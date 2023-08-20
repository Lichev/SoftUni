money = 0
validation = False
while True:
    command = input()
    if command == 'special':
        validation = True
    if command == 'special' or command == 'regular':
        break

    data = float(command)

    if data >= 0:
        money += data
    else:
        print(f'Invalid price!')

taxes = money * 0.20
total = money + taxes
if total > 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {money:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'----------- ')

    if validation:
        print(f'Total price: {total - (total * 0.10):.2f}$')
    else:
        print(f'Total price: {total:.2f}$')
else:
    print(f'Invalid order!')
def loading(number):
    if number == 100:
        print(f'100% Complete!')
    else:
        print(f'{number}% ', end='')
    print(f'[', end='')

    current = number / 10
    for i in range(1, 10 + 1):
        if i <= current:
            print(f'%', end='')
        else:
            print(f'.', end='')
    print(f']', end='')

    if current < 10:
        print(f"\nStill loading...")


num = int(input())
loading(num)

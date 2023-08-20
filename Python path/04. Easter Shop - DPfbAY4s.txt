in_the_store = int(input())

eggs = in_the_store
sold = 0
allowed = 0


while eggs > 0:
    command = input()

    if command == 'Close':
        print(f"Store is closed!")
        print(f"{sold} eggs sold.")
        break

    number = int(input())

    if number > eggs:
        allowed = number

    if command == 'Buy':
        if number > eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            break
        eggs -= number
        sold += number
    elif command == 'Fill':
        eggs += number

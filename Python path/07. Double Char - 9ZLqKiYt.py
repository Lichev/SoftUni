while True:
    str = input()

    if str == 'End':
        break

    if str == 'SoftUni':
        continue
    else:
        for i in range(len(str)):
            print(str[i] * 2, end='')

        print(f'')
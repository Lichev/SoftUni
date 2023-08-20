text = [text.strip() for text in input().split(", ")]

valid = False
if_win = False
for i in text:
    if len(i) == 20:
        valid = True

    if valid:
        first_half = i[:10]
        second_half = i[10:]
        special = ''

        symbols = ['@', '#', '$', '^']

        for char in symbols:
            for rep in range(10, 5, -1):
                winning = char * rep
                if winning in first_half and winning in second_half:
                    if rep == 10:
                        print(f'ticket "{i}" - {rep}{char} Jackpot!')
                        if_win = True
                        break
                    else:
                        print(f'ticket "{i}" - {rep}{char}')
                        if_win = True
                        break

        if not if_win:
            print(f'ticket "{i}" - no match')

    else:
        print(f'invalid ticket')

    valid = False
    if_win = False
sold_games = int(input())

Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0


for i in range(sold_games):
    name = input()

    if name == 'Hearthstone':
        Hearthstone +=1
    elif name == 'Fornite':
        Fornite += 1
    elif name == 'Overwatch':
        Overwatch += 1
    else:
        Others += 1


print(f'Hearthstone - {(Hearthstone / sold_games) * 100:.2f}%')
print(f'Fornite - {(Fornite  / sold_games) * 100:.2f}%')
print(f'Overwatch - {(Overwatch / sold_games) * 100:.2f}%')
print(f'Others - {(Others / sold_games) * 100:.2f}%')

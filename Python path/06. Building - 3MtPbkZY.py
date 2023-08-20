floors = int(input())
rooms = int(input())

count = 0
neshto = ''

for i in range(floors, 0, -1):
    for k in range(rooms):
        count = i * 10 + k

        if i == floors:
            neshto = 'L'
        elif i % 2 == 0:
            neshto = 'O'
        else:
            neshto = 'A'

        print(f'{neshto}{count}', end=' ')
    print('')

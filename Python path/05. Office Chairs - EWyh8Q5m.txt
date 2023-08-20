number_of_rooms = int(input())

free_chairs = 0
validation = False

for x in range(1,number_of_rooms + 1):
    current = input().split(' ')
    chairs = len(current[0])
    visitors = int(current[1])

    if chairs < visitors:
        print(f'{visitors - chairs} more chairs needed in room {x}')
        validation = True
    else:
        free_chairs += chairs - visitors

if not validation:
    print(f'Game On, {free_chairs} free chairs left')


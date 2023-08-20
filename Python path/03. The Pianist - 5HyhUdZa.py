def add(dict, piece, composer, key):
    if piece not in dict:
        dict[piece] = {}
        dict[piece]['composer'] = composer
        dict[piece]['key'] = key
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f'{piece} is already in the collection!')
    return dict


def remove(dict, piece):
    if piece in dict:
        del dict[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return dict


def changekey(dict, piece, new_key):
    if piece in dict:
        dict[piece]['key'] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return dict


num = int(input())

dict = {}

for i in range(num):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]

    dict[piece] = {}
    dict[piece]['composer'] = composer
    dict[piece]['key'] = key

command = input()

while command != 'Stop':
    command = command.split("|")
    action = command[0]

    if action == 'Add':
        add_piece = command[1]
        add_composer = command[2]
        add_key = command[3]
        dict = add(dict, add_piece,add_composer,add_key)

    elif action == 'Remove':
        remove_piece = command[1]
        dict = remove(dict, remove_piece)

    elif action == 'ChangeKey':
        change_piece = command[1]
        new_key = command[2]
        dict = changekey(dict, change_piece, new_key)

    command = input()

for primery_key in dict.keys():
    print(f"{primery_key} -> ", end='')
    for key, value in dict[primery_key].items():
        if key == 'composer':
            print(f'Composer: {value}, ', end='')
        else:
            print(f'Key: {value}', end="")
    print('')

def flights(*args):
    dct = {}
    last_destionation = ''
    for x in range(len(args)):
        current_item = args[x]
        if args[x] == 'Finish':
            break
        else:
            if x == 0:
                dct[current_item] = 0
                last_destionation = current_item
            elif x % 2 != 0:
                dct[last_destionation] += current_item
            else:
                last_destionation = current_item
                if current_item not in dct:
                    dct[current_item] = 0

    return  dct

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))


# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
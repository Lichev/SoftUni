my_dict = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk = {}
shards_valid = False
fragments_valid = False
motes_valid = False

while True:
    command = input().split(" ")

    for i in range(0, len(command), 2):
        quantity = int(command[i])
        material = command[i + 1].lower()
        if material == 'shards' or material == 'fragments' or material == 'motes':
            my_dict[material] += quantity

            if 'shards' in my_dict and my_dict['shards'] >= 250:
                shards_valid = True
                break
            if 'fragments' in my_dict and my_dict['fragments'] >= 250:
                fragments_valid = True
                break
            if 'motes' in my_dict and my_dict['motes'] >= 250:
                motes_valid = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if shards_valid or fragments_valid or motes_valid:
        break

if shards_valid:
    my_dict['shards'] -= 250
    print(f'Shadowmourne obtained!')
    [print(f'{key}: {value}') for key, value in my_dict.items()]
    [print(f'{key}: {value}') for key, value in junk.items()]
elif fragments_valid:
    my_dict['fragments'] -= 250
    print(f'Valanyr obtained!')
    [print(f'{key}: {value}') for key, value in my_dict.items()]
    [print(f'{key}: {value}') for key, value in junk.items()]
elif motes_valid:
    my_dict['motes'] -= 250
    print(f'Dragonwrath obtained!')
    [print(f'{key}: {value}') for key, value in my_dict.items()]
    [print(f'{key}: {value}') for key, value in junk.items()]

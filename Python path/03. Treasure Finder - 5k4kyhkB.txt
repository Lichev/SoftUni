key = [int(i) for i in input().split(" ")]

command = input()


while command != 'find':
    counter = 0
    new_text = ''
    for char in command:
        if counter >= len(key):
            counter = 0

        current = ord(char) - key[counter]
        new_text += chr(current)
        counter += 1
    treasure = ''
    treasure_find = ''
    coordinate = ''
    coordinate_find = ''

    for info in new_text:
        if info == '&':
            treasure_find += '&'
        if info == '<':
            coordinate_find = '<'
        if info == '>':
            coordinate_find = '>'

        if treasure_find == "&" and info != "&":
            treasure += info
        if coordinate_find == "<" and info != "<":
            coordinate += info

    print(f'Found {treasure} at {coordinate}')

    command = input()

number = int(input())

for i in range(number):
    text = input()
    start_end_name = ''
    start_end_age = ''
    name = ""
    age = ''

    for char in text:

        if char == '@':
            start_end_name = '@'
        if char == '|':
            start_end_name = '|'
        if char == '#':
            start_end_age = '#'
        if char == '*':
            start_end_age = '*'

        if start_end_name == '@' and char != '@':
            name += char
        if start_end_age == '#' and char != '#':
            age += char

    print(f"{name} is {age} years old.")
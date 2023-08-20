def take_odd(text):
    new_text = ''

    for i in range(len(text)):
        if i % 2 != 0:
            new_text += text[i]

    return new_text


def cut(text, index, lenght):
    to_remove = text[index: index + lenght]
    text = text.replace(to_remove, "", 1)
    return text


def substitute(text, old, new):
    if old in text:
        text = text.replace(old, new)
        print(text)
    else:
        print('Nothing to replace!')

    return text


text = input()
command = input()

while command != 'Done':
    command = command.split(" ")
    data = command[0]

    if data == 'TakeOdd':
        text = take_odd(text)
        print(text)
    elif data == 'Cut':
        index = int(command[1])
        lenght = int(command[2])
        text = cut(text, index, lenght)
        print(text)
    elif data == 'Substitute':
        old = command[1]
        new = command[2]
        text = substitute(text, old, new)

    command = input()

print(f'Your password is: {text}')
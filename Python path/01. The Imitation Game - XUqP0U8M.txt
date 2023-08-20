text = input()

command = input()

while command != 'Decode':
    data = command.split("|")
    action = data[0]

    if action == 'Move':
        number_of_letters = int(data[1])
        take = text[:number_of_letters]
        left = text[number_of_letters :]
        text = left + take

    elif action == 'Insert':
        index = int(data[1])
        value = data[2]
        text = text[:index] + value + text[index:]

    elif action == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        text = text.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {text}')
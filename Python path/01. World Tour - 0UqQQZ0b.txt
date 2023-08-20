def valid_index(text, index):
    validation = False

    if 0 <= index < len(text):
        validation = True

    return validation


text = input()

command = input()

while command != 'Travel':
    command = command.split(":")
    action = command[0]

    if action == 'Add Stop':
        add_index = int(command[1])
        valid_add_index = valid_index(text, add_index)
        add_stop = command[2]

        if valid_add_index:
            text = text[:add_index] + add_stop + text[add_index:]


    elif action == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        valid_start = valid_index(text, start_index)
        valid_end = valid_index(text, end_index)

        if valid_start and valid_end:
            remove_text = text[start_index:end_index + 1]
            text = text.replace(remove_text, "", 1)


    elif action == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)

    command = input()

print(f"Ready for world tour! Planned stops: {text}")
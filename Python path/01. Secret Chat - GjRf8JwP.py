message = input()

command = input()

while command != 'Reveal':
    command = command.split(":|:")
    action = command[0]

    if action == 'InsertSpace':
        insert_index = int(command[1])
        message = message[:insert_index] + ' ' + message[insert_index:]
        print(message)

    elif action == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print("error")
    elif action == 'ChangeAll':
        old = command[1]
        new = command[2]
        message = message.replace(old, new)
        print(message)


    command = input()

print(f'You have a new text message: {message}')
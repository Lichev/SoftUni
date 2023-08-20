text = input()


command = input()

while command != 'Generate':
    command = command.split('>>>')

    action = command[0]

    if action == 'Contains':
        substring = command[1]

        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print(f'Substring not found!')

    elif action == 'Flip':
        next_action = command[1]
        startIndex = int(command[2])
        endIndex = int(command[3])

        if next_action == 'Upper':
            first_part = text[:startIndex]
            to_change = text[startIndex:endIndex]
            second_part = text[endIndex:]

            to_change = to_change.upper()

            text = first_part + to_change + second_part
        else:
            first_part = text[:startIndex]
            to_change = text[startIndex:endIndex]
            second_part = text[endIndex:]

            to_change = to_change.lower()

            text = first_part + to_change + second_part

        print(text)

    elif action == 'Slice':
        del_start = int(command[1])
        del_end = int(command[2])

        first_text = text[:del_start]
        del_text = text[del_start:del_end]
        second_text = text[del_end:]
        text = first_text + second_text

        print(text)

    command = input()

print(f"Your activation key is: {text}")
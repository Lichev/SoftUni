count = 0
if_valid = False
while True:
    event = input()

    if event == 'END':
        break
    new_event = event.lower()
    if new_event == 'coding' or new_event == 'dog' or new_event == 'cat' or new_event == 'movie':
        if_valid = event.islower()

        if if_valid:
            count += 1
        else:
            count += 2


if count <= 5:
    print(count)
else:
    print(f'You need extra sleep')
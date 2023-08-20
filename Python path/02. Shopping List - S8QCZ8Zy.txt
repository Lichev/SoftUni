list_of_groceries = input().split('!')

while True:
    command = input()

    if command == 'Go Shopping!':
        break

    data = command.split(" ")
    action = data[0]
    item = data[1]

    if action == 'Urgent':
        if item not in list_of_groceries:
            list_of_groceries.insert(0, item)
    elif action == 'Unnecessary':
        list_of_groceries = [i for i in list_of_groceries if i not in item]
    elif action == 'Correct':
        if item in list_of_groceries:
            new_item = data[2]
            for index, i in enumerate(list_of_groceries):
                if i == item:
                    list_of_groceries[index] = new_item
                    break
    elif action == 'Rearrange':
        if item in list_of_groceries:
            for index, i in enumerate(list_of_groceries):
                if i == item:
                    list_of_groceries.append(item)
                    list_of_groceries.pop(index)
                    break

print(", ".join(list_of_groceries))

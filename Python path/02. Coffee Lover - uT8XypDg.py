def include(current, coffees):
    coffees.append(current)
    return coffees


def remove(action, ranges, coffees):
    count = 0
    new_list = []
    if action == 'first':
        for i in range(ranges):
            new_list.append(coffees[count])
            count += 1
    else:
        for s in range(ranges):
            count += 1
            new_list.append(coffees[-count])
    coffees = [cur for cur in coffees if cur not in new_list]
    return coffees


def prefer(first, second, coffees):
    validation = 0 <= first < len(coffees) and 0 <= second < len(coffees)

    if validation:
        coffees[first], coffees[second] = coffees[second], coffees[first]

    return coffees


def reverse_list(coffees):
    coffees = reversed(coffees)

    return coffees


def general(coffees, orders):
    for i in range(orders):
        command = input().split(" ")
        action = command[0]

        if action == 'Include':
            coffee = command[1]
            coffees = include(coffee, coffees)
        elif action == 'Remove':
            first_or_last = command[1]
            ranges = int(command[2])
            coffees = remove(first_or_last, ranges, coffees)
        elif action == 'Prefer':
            first_index = int(command[1])
            second_index = int(command[2])
            coffees = prefer(first_index, second_index, coffees)
        elif action == 'Reverse':
            coffees = reverse_list(coffees)

    print(f"Coffees:\n{' '.join(coffees)}")


coffee_list = input().split(' ')
n = int(input())
general(coffee_list, n)

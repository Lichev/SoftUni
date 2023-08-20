from collections import deque


def fill_the_box(*args):
    size_of_box = args[0:3]

    def multiply():
        result = 1

        for x in size_of_box:
            result *= x

        return result

    free_space = multiply()
    rest_of_args = args[3:]
    check = deque(rest_of_args)

    while free_space > 0:
        current = check.popleft()

        if current == 'Finish':
            break

        if free_space >= current:
            free_space -= current
        elif current > free_space:
            remnant = current - free_space
            free_space = free_space - (current - remnant)
            check.append(remnant)

    left_cubes = [x for x in check if x != 'Finish']
    sum_cubes = sum(left_cubes)

    if free_space > 0:
        return f"There is free space in the box. You could put {free_space} more cubes."
    else:
        return f"No more free space! You have {sum_cubes} more cubes."



print(fill_the_box(2, 8,2, 2, 1, 7, 3, 1, 5,"Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
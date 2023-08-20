course_program = input().split(", ")


def find_index(current):
    index1 = 0
    for index, i in enumerate(course_program):
        if current == i:
            index1 = index
    return index1


command = input()
while command != 'course start':
    data = list(command.split(":"))

    action = data[0]
    lesson = data[1]

    if action == 'Insert':
        index = int(data[2])
        if lesson not in course_program:
            course_program.insert(index, lesson)
    elif action == 'Add':
        if lesson not in course_program:
            course_program.append(lesson)
    elif action == 'Remove':
        if lesson in course_program:
            course_program.remove(lesson)
        check = lesson + '-Exercise'
        if check in course_program:
            course_program.remove(check)
    elif action == 'Swap':
        lesson2 = data[2]
        a = find_index(lesson)
        b = find_index(lesson2)
        course_program[a], course_program[b] = course_program[b], course_program[a]
        check1 = lesson + '-Exercise'
        check2 = lesson2 + '-Exercise'

        if check1 in course_program:
            course_program.remove(check1)
            course_program.insert(b + 1, check1)
        elif check2 in course_program:
            course_program.remove(check2)
            course_program.insert(a + 1, check2)

    elif action == 'Exercise':
        lesson2 = lesson + '-Exercise'
        if lesson in course_program and lesson2 not in course_program:
            a = find_index(lesson)
            course_program.insert(a+1, lesson2)
        elif lesson not in course_program:
            course_program.append(lesson)
            course_program.append(lesson2)

    command = input()

for (i, item) in enumerate(course_program, start=1):
    print (f"{i}.{item}")
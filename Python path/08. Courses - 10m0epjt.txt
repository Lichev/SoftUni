from collections import defaultdict

command = input()

my_dict = defaultdict(list)

while command != 'end':
    data = command.split(" : ")
    course = data[0]
    student = data[1]

    if course not in my_dict.keys():
        my_dict[course] = []

    my_dict[course].append(student)

    command = input()


for value, key in my_dict.items():
    print(f"{value}: {len(key)}")
    for i in key:
        print(f'-- {i}')
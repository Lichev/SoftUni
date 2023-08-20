students_dict = {}
command = input()

while ':' in command:
    data = command.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

course = " ".join(command.split("_"))

for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')
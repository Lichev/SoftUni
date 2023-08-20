my_dict = {}
number = 0
while True:
    command = input()

    if command.isdigit():
        number = int(command)
        break

    data = command.split("-")
    name = data[0]
    number = data[1]

    my_dict[name] = number


for i in range(number):
    name_of_person = input()

    if name_of_person in my_dict.keys():
        print(f'{name_of_person} -> {my_dict[name_of_person]}')
    else:
        print(f"Contact {name_of_person} does not exist.")

from collections import defaultdict

command = input()

mydict = defaultdict(list)

while command != 'End':
    data = command.split(" -> ")
    company = data[0]
    employee = data[1]

    if company not in mydict.keys():
        mydict[company] = []

    if employee not in mydict[company]:
        mydict[company].append(employee)

    command = input()

for key, value in mydict.items():
    print(f'{key}')
    [print(f'-- {i}') for i in value]

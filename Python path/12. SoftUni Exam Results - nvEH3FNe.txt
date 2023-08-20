command = input()
points = {}
submissions = {}

while command != 'exam finished':
    data = command.split("-")
    name = data[0]
    parameter = data[1]

    if parameter == 'banned':
        if name in points.keys():
            del points[name]
    else:
        score = int(data[2])

        if parameter not in submissions.keys():
            submissions[parameter] = 0
        submissions[parameter] += 1

        if name not in points.keys():
            points[name] = 0

        if points[name] < score:
            points[name] = score

    command = input()

print(f'Results:')
[print(f'{key} | {value}') for key, value in points.items()]
print(f'Submissions:')
[print(f'{key} - {value}') for key, value in submissions.items()]
from collections import OrderedDict

command = input()

info = {}

while command != 'end of contests':
    command = command.split(":")
    contest = command[0]
    password = command[1]

    info[contest] = password

    command = input()

submissions = input()

sub_info = {}
while submissions != "end of submissions":
    submissions = submissions.split("=>")
    sub_contest = submissions[0]
    sub_password = submissions[1]
    username = submissions[2]
    points = int(submissions[3])
    valid = False

    if sub_contest in info:
        valid = info[sub_contest] == sub_password

    if valid:
        if username not in sub_info:
            sub_info[username] = {}

        if sub_contest not in sub_info[username]:
            sub_info[username][sub_contest] = points
        else:
            if points > sub_info[username][sub_contest]:
                sub_info[username][sub_contest] = points

    submissions = input()

sub_info = OrderedDict(sorted(sub_info.items())) #sort alphabetical


total_info = {}
for s in sub_info.keys():
    for k, v in sub_info[s].items():
        if s not in total_info:
            total_info[s] = v
        else:
            total_info[s] += v

total_info = dict(sorted(total_info.items(), key=lambda item: item[1], reverse=True)) #
best = list(total_info.items())[0]


print(f'Best candidate is {best[0]} with total {best[1]} points.')
print(f'Ranking:')
for primary in sub_info.keys():
    sub_info[primary] = dict(sorted(sub_info[primary].items(), key=lambda item: item[1], reverse=True)) #take and print the keys in desc order
    print(primary)
    [print(f'#  {key} -> {value}') for key, value in sub_info[primary].items()]

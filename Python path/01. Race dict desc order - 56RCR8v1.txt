import re

racers = list(input().split(", "))

command = input()

letters = r'[A-Za-z]'
digits = r'[0-9]'
race = {}

while command != 'end of race':
    matches_letters = re.findall(letters, command)
    match_digits = re.findall(digits, command)
    name = "".join(matches_letters)
    distance = [sum(int(i) for i in match_digits)]

    if name in racers:
        if name not in race:
            race[name] = sum(distance)
        else:
            race[name] += sum(distance)

    command = input()


sorted_dict = dict(sorted(race.items(), key=lambda item: item[1], reverse=True))
key_list = list(sorted_dict)

print(f'1st place: {key_list[0]}')
print(f'2nd place: {key_list[1]}')
print(f'3rd place: {key_list[2]}')
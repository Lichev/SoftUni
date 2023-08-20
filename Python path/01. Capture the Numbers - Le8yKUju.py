import re


while True:
    command = input()
    if not command:
        break

    rex = r'(?P<numbers>[0-9]+)'
    matches = re.findall(rex, command)

    for match in matches:
        num = match
        print(num, end= " ")

import re

names = input()
rex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(rex, names)

for match in matches:
    print(match.group(), end=" ")
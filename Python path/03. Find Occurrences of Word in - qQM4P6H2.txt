import re
command = input().lower()
find = input().lower()
path = fr'{find}(?!\w+)'
matches = re.findall(path, command)


print(len(matches))

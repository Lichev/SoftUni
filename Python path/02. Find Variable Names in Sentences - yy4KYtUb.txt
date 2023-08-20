import re
command = input()


rex = r'(?<!__)(?<=_)([a-zA-Z0-9]+)(?=\s|$)'
matches = re.findall(rex, command)


print(",".join(matches))
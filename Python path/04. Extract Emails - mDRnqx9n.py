import re

command = input()

rex = r'(?<=\s)(?P<user>[a-zA-Z][a-zA-Z\.\-\_]*)+@(?P<host>[a-zA-Z\-]+[\.][a-zA-z\.]+)\b'
matches = re.finditer(rex, command)

mail_list = []

for match in matches:
    user = match.group('user')
    host = match.group('host')

    print(f'{user}@{host}')

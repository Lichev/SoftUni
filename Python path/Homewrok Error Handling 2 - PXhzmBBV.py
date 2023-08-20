import re


class NameTooShortError(Exception):
    """"Less characters"""


class MustContainAtSymbolError(Exception):
    """It doesn't have @"""

class InvalidDomainError(Exception):
    """Invalid domain"""

class NoMatches(Exception):
    """No Matches"""

class InvalidIndex(Exception):
    """No Matches"""



command = input()
valid_domains = ['.com', ".bg", ".org," ".net"]

while command != 'End':
    sample = r'([a-zA-Z]+)@?(\w+)(\.[\w+]+)'
    result = re.findall(sample, command)

    if not result:
        raise NoMatches(f'There is no matches')

    if len(result[0]) < 2:
        raise InvalidIndex('No valid index')
    name = result[0][0]
    domain = result[0][2]

    if '@' not in command:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    command = input()
import  re

names = input()
rex = r"\b(?P<day>[0-9]{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[0-9]{4})\b"
matches = re.finditer(rex, names)

for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")
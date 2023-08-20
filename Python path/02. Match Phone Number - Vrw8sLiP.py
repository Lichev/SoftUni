import  re

names = input()
rex = r"(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b"
matches = re.findall(rex, names)

print(", ".join(matches))
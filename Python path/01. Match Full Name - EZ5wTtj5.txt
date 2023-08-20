import  re

names = input()
rex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(rex, names)

print(" ".join(matches))
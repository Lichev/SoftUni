import re

text = input()

sample = r'(#|@)(?P<A>[A-Za-z]{3,})(\1)(\1)(?P<B>[A-Za-z]{3,})(\1)'
matches = re.finditer(sample, text)
validation = re.findall(sample, text)

list_of_pairs = []

for match in matches:
    a = match.group('A')
    b = match.group('B')

    if a == b[::-1]:
        text_to_append = a + " <=> " + b
        list_of_pairs.append(text_to_append)

if len(validation) > 0:
    print(f"{len(validation)} word pairs found!")
else:
    print(f"No word pairs found!")

if len(list_of_pairs) > 0:
    print(f'The mirror words are:')
    print(", ".join(list_of_pairs))
else:
    print(f"No mirror words!")
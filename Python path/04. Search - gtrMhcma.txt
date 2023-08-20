n = int(input())
key = input()

strings = list()
filters = list()

for i in range(n):
    words = input()
    strings.append(words)

    if key in words:
        filters.append(words)

print(strings)
print(filters)
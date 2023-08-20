numbers = tuple(map(float, input().split(" ")))

d = {}

for i in numbers:
    if i not in d:
        d[i] = 0

    d[i] += 1

[print(f'{v} - {k} times') for v, k in d.items()]
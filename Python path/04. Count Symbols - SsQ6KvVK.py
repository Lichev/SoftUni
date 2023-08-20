text = input()

d = {}

for i in text:
    if i not in d:
        d[i] = 0

    d[i] += 1


[print(f'{key}: {value} time/s') for key,value in sorted(d.items())]



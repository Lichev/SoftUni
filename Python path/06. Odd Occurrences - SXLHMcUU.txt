vhod = input().split(" ")

neshto = {}

for i in vhod:
    i = i.lower()

    if i not in neshto:
        neshto[i] = 1
    else:
        neshto[i] += 1

filters = {lan:values for (lan, values) in neshto.items() if values % 2 != 0}
print(" ".join(filters.keys()))
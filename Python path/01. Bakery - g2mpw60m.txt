vhod = input().split(" ")
bakery = {}

for i in range(0, len(vhod), 2):
    key = vhod[i]
    value = int(vhod[i + 1])
    bakery[key] = value

print(bakery)
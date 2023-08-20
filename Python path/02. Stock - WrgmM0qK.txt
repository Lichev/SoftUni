vhod = input().split(" ")
search = input().split(" ")

available = {}

for i in range(0, len(vhod), 2):
    key = vhod[i]
    value = vhod[i + 1]

    available[key] = int(value)


for k in search:
    if k in available:
        print(f'We have {available.get(k)} of {k} left')
    else:
        print(f"Sorry, we don't have {k}")
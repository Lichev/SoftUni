from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

dct = {
    "Diamond Jewellery": 0,
    "Gold": 0,
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
}
Gemstone = 0
Porcelain_Sculpture = 0
Gold = 0
Diamond_Jewellery = 0

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = material + magic

    if result < 100:
        if result % 2 == 0:
            material = material * 2
            magic = magic * 3
            result = material + magic
        else:
            result = result * 2
    elif result >= 500:
        result = result / 2

    if 100 <= result < 200:
        dct["Gemstone"] += 1
    elif 200 <= result < 300:
        dct["Porcelain Sculpture"] += 1
    elif 300 <= result < 400:
        dct["Gold"] += 1
    elif 400 <= result < 500:
        dct["Diamond Jewellery"] += 1

final = sorted(dct.items(), key=lambda x: x[0])


if dct["Gemstone"] > 0 and dct["Porcelain Sculpture"] > 0 or dct["Gold"] > 0 and dct["Diamond Jewellery"] > 0:
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in final:
    if value > 0:
        print(f"{key}: {value}")
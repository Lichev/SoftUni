from collections import deque

dict = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

doll = 150
wooden_train = 250
teddy_bear = 300
bicycle = 400

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

while True:
    if not magic:
        break
    if not materials:
        break
    
    valid = False
    
    if magic[0] == 0:
        magic.popleft()
        valid = True
    if materials[-1] == 0:
        materials.pop()
        valid = True
        
    if valid:
        continue

    present = ''
    current_magic = magic[0]
    current_material = materials[-1]

    result = current_magic * current_material

    valid = False

    if result == doll:
        present = 'Doll'
        dict[present] += 1
        magic.popleft()
        materials.pop()
        valid = True
    elif result == wooden_train:
        present = 'Wooden train'
        dict[present] += 1
        magic.popleft()
        materials.pop()
        valid = True
    elif result == teddy_bear:
        present = 'Teddy bear'
        dict[present] += 1
        magic.popleft()
        materials.pop()
        valid = True
    elif result == bicycle:
        present = 'Bicycle'
        dict[present] += 1
        magic.popleft()
        materials.pop()
        valid = True

    if result < 0:
        to_add = magic.popleft() + materials.pop()
        materials.append(to_add)

    if not valid and result > 0:
        magic.popleft()
        materials[-1] += 15


if dict['Doll'] > 0 and dict['Wooden train'] > 0:
    print(f"The presents are crafted! Merry Christmas!")
elif dict['Teddy bear'] > 0 and dict['Bicycle'] > 0:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

materials.reverse()

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

[print(f"{key}: {value}") for key, value in sorted(dict.items()) if value > 0]

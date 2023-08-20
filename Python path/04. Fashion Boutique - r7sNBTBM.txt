box_of_clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())


racks = list()

current_rack = 0

while box_of_clothes:
    current = box_of_clothes.pop()

    if current + current_rack < capacity_of_rack:
        current_rack += current
    elif current_rack + current > capacity_of_rack:
        racks.append(1)
        current_rack = current
    elif current_rack + current == capacity_of_rack:
        racks.append(1)
        current_rack = 0

if current_rack > 0:
    racks.append(1)

print(len(racks))
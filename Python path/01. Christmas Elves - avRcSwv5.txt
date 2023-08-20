from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials_box = [int(x) for x in input().split()]

total_number_of_toys = 0
total_used_energy = 0
rounds = 0

while elf_energy and materials_box:
    elf = elf_energy.popleft()

    if elf < 5:
        continue

    box = materials_box.pop()
    current_toys_made = 0
    rounds += 1

    if elf >= box:
        if rounds % 3 == 0:
            if elf >= box * 2:
                current_toys_made += 2
                total_used_energy += box * 2
                elf_energy.append((elf - (box * 2)) + 1)
            else:
                materials_box.append(box)
                elf_energy.append(elf * 2)
                continue
        elif rounds > 0:
            current_toys_made += 1
            total_used_energy += box
            elf_energy.append((elf - box) + 1)

        if rounds % 5 == 0:
            current_toys_made = 0
            elf_energy[-1] -= 1


        total_number_of_toys += current_toys_made
    else:
        materials_box.append(box)
        elf_energy.append(elf * 2)


print(f"Toys: {total_number_of_toys}")
print(f'Energy: {total_used_energy}')

if elf_energy:
    print(f'Elves left: {", ".join(map(str, elf_energy))}')
if materials_box:
    print(f'Boxes left: {", ".join(map(str, materials_box))}')
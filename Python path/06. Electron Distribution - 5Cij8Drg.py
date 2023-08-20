electrons = int(input())
count = 1
new_list = []

while electrons > 0:
    maximum_electrons = 2 * count ** 2
    if electrons - maximum_electrons < 0:
        new_list.append(electrons)
    else:
        new_list.append(maximum_electrons)
    electrons -= maximum_electrons
    count += 1

print(new_list)
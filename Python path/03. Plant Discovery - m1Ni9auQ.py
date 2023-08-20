n = int(input())

dict = {}

for i in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])

    if plant not in dict:
        dict[plant] = {}

    dict[plant]["Rarity"] = rarity
    dict[plant]["Rating"] = []


command = input()
while command != 'Exhibition':
    data = command.split(": ")
    action = data[0]

    if action == "Rate":
        another_data = data[1].split(" - ")
        current_plant = another_data[0]
        rating = int(another_data[1])

        if current_plant in dict:
            dict[current_plant]["Rating"].append(rating)
        else:
            print(f'error')
    elif action == 'Update':
        another_data = data[1].split(" - ")
        current_plant = another_data[0]
        new_rarirty = int(another_data[1])

        if current_plant in dict:
            dict[current_plant]["Rarity"] = new_rarirty
        else:
            print(f'error')
    elif action == 'Reset':
        current_plant = data[1]
        if current_plant in dict:
            dict[current_plant]["Rating"].clear()
        else:
            print(f'error')

    command = input()

print(f'Plants for the exhibition:')
for primery_key in dict.keys():
    print(f"- {primery_key}; ", end='')
    for key, value in dict[primery_key].items():
        if key == 'Rarity':
            print(f"{key}: {value};", end= '')
        else:
            if sum(value) == 0:
                print(f" {key}: 0.00", end='')
                pass
            else:
                print(f" {key}: {(sum(value) / len(value)):.2f}", end='')
    print(f'')
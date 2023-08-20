product = input().split('#')
water = int(input())

cells = list()
fire = list()
for current in product:
    new_list = current.split(" ")

    if_is_valid = False
    level = new_list[0]
    ranger = int(new_list[2])

    if level == 'High' and 81 <= ranger <= 125:
        if_is_valid = True
    elif level == "Medium" and 51 <= ranger <= 80:
        if_is_valid = True
    elif level == "Low" and 1 <= ranger <= 50:
        if_is_valid = True
    else:
        if_is_valid = False
        continue

    if if_is_valid and (water >= ranger):
        water -= ranger
        fire.append(ranger)
    else:
        continue

print("Cells:")
for i in fire:
    print(f" - {i}")
print(f"Effort: {sum(fire) * 0.25:.2f}")
print(f'Total Fire: {sum(fire)}')
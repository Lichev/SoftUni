lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_count = 0
sword_count = 0
shield_count = 0
sword_broken = False
helmet_broken = False
armor_count = 0


for i in range(1, lost_fights+1):
    if i % 2 == 0:
        helmet_count += 1
        helmet_broken = True

    if i % 3 == 0:
        sword_count += 1
        sword_broken = True

    if sword_broken and helmet_broken:
        shield_count += 1
        if shield_count % 2 == 0:
            armor_count += 1

    sword_broken = False
    helmet_broken = False

print(f'Gladiator expenses: {helmet_count * helmet_price + sword_price * sword_count + shield_count * shield_price + armor_count * armor_price:.2f} aureus')
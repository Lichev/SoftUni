quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0
is_valid = False

for i in range(1, days + 1):
    is_valid = False
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        total_cost += 2 * quantity
        total_spirit += 5
    if i % 3 == 0:
        total_cost += (quantity * 5) + (quantity * 3)
        total_spirit += 3 + 10
        is_valid = True
    if i % 5 == 0:
        total_cost += quantity * 15
        total_spirit += 17
        if is_valid:
            total_spirit += 30

    if i % 10 == 0:
        total_spirit -= 20
        total_cost += 5 + 3 + 15

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

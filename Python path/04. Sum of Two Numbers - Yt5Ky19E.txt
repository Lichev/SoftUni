start_from = int(input())
end_to = int(input())
magic_number = int(input())

count = 0
result = 0
is_true = False

for i in range(start_from, end_to + 1):
    for k in range(start_from, end_to + 1):
        count += 1
        result = i + k

        if result == magic_number:
            is_true = True
            break
    if is_true:
        break

if is_true:
    print(f"Combination N:{count} ({i} + {k} = {magic_number})")
else:
    print(f"{count} combinations - neither equals {magic_number}")
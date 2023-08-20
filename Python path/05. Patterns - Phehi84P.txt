number = int(input())

for i in range(1 , number + 1):
    for j in range(1, i + 1):
        print(f'*', end='')
    print()

for k in range(number, 1, -1):
    for j in range(k-1):
        print(f"*", end='')
    print()
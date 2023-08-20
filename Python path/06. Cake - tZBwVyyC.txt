lenght = int(input())
weight = int(input())

whole_cake = lenght * weight

while whole_cake > 0:
    take = input()

    if take == 'STOP':
        break

    k = int(take)
    whole_cake -= k

result = abs(whole_cake)
if whole_cake < 0:
    print(f"No more cake left! You need {result} pieces more.")
else:
    print(f"{result} pieces are left.")
n = int(input())

s = set()

for i in range(n):
    action , car = input().split(", ")

    if action == 'IN':
        s.add(car)
    else:
        s.remove(car)

if s:
    print("\n". join(s))
else:
    print(f'Parking Lot is Empty')
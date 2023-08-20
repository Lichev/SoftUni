money = float(input())


all = int(money * 100)
count = 0

while all > 0:

    if all >= 200:
        all -= 200
    elif all >= 100:
        all -= 100
    elif all >= 50:
        all -= 50
    elif all >= 20:
        all -= 20
    elif all >= 10:
        all -= 10
    elif all >= 5:
        all -= 5
    elif all >= 2:
        all -= 2
    elif all >= 1:
        all -= 1

    count += 1

print(count)

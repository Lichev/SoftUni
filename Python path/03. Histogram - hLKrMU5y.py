n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
all = 0


for i in range(n):
    number = int(input())
    all += 1

    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1


print(f'{(p1 / all) * 100:.2f}%')
print(f'{(p2 / all) * 100:.2f}%')
print(f'{(p3 / all) * 100:.2f}%')
print(f'{(p4 / all) * 100:.2f}%')
print(f'{(p5 / all) * 100:.2f}%')

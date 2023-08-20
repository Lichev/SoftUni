n = int(input())

points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
outside = 0
delene = 0

for i in range(n):
    colors = input()

    if colors == 'red':
        points += 5
        red += 1
    elif colors == 'orange':
        points += 10
        orange += 1
    elif colors == 'yellow':
        points += 15
        yellow += 1
    elif colors == 'white':
        points += 20
        white += 1
    elif colors == 'black':
        points /= 2
        black += 1
        delene += 1
    else:
        outside += 1

print(f"Total points: {int(points)}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {outside}")
print(f"Divides from black balls: {delene}")

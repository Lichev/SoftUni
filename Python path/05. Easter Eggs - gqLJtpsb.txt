number_of_eggs = int(input())

orange = 0
red = 0
blue = 0
green = 0

for i in range(number_of_eggs):
    color = input()

    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
if orange > red and orange > blue and orange > green:
    print(f'Max eggs: {orange} -> orange')
elif red > orange and red > blue and red > green:
    print(f'Max eggs: {red} -> red')
elif blue > green and blue > orange and blue > red:
    print(f'Max eggs: {blue} -> blue')
else:
    print(f'Max eggs: {green} -> green')




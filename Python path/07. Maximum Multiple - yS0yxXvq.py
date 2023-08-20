divisor = int(input())
boundary = int(input())

number = 0

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        number = i
        break

print(number)
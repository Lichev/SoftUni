capacity = int(input())
elevate = int(input())

count = 0

while capacity > 0:
    capacity -= elevate
    count += 1

print(count)
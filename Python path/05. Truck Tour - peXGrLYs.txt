from collections import deque

n = int(input())

info = deque()

for i in range(n):
    data = [int(x) for x in input().split()]
    info.append(data)

for attemps in range(n):
    needed = 0
    valid = False
    for petrol, distance in info:
        needed = needed + petrol - distance

        if needed < 0:
            valid = True
            break

    if valid:
        info.append(info.popleft())
    else:
        print(attemps)
        break

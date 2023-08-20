from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())


collected = 0

while True:

    if not bees:
        break
    if not nectar:
        break

    current_bee = bees[0]
    current_nectar = nectar[-1]
    sign = symbols[0]

    if current_bee > current_nectar:
        nectar.pop()
        continue
    else:
        result = 0
        bees.popleft()
        nectar.pop()
        symbols.popleft()

        if sign == '+':
            result = current_bee + current_nectar
        elif sign == '-':
            result = current_bee - current_nectar
        elif sign == '*':
            result = current_bee * current_nectar
        elif sign == '/':
            if current_bee == 0 or current_nectar == 0:
                continue
            result = current_bee / current_nectar

        collected += abs(result)

print(f"Total honey made: {collected}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
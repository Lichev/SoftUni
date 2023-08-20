from collections import deque

males = deque(map(int, input().split(" ")))
females = deque(map(int, input().split(" ")))
matches = 0

while males and females:

    if males[-1] <= 0:
        males.pop()
        continue
    elif females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    elif females[-1] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    he = males.pop()
    she = females.popleft()

    if he == she:
        matches += 1
    else:
        males.append(he - 2)

r = list(reversed(males))

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, r))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join((map(str, females)))}")
else:
    print(f"Females left: none")



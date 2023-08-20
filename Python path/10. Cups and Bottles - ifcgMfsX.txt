from collections import deque

cups = deque(int(c) for c in input().split())
bottles = [int(b) for b in input().split()]

used_bottles = 0
wasted_water = 0

while True:

    if not cups:
        break
    if not bottles:
        break

    current_cup = cups[0]
    current_bottle = bottles[-1]

    if current_bottle <= 0:
        bottles.pop()


    if current_cup > current_bottle:
        cups[0] -= bottles[-1]
        bottles.pop()
        used_bottles +=1
    elif current_cup == current_bottle:
        used_bottles += 1
        cups.popleft()
        bottles.pop()
    elif current_cup < current_bottle:
        waste = current_bottle - current_cup
        cups.popleft()
        bottles.pop()
        used_bottles += 1
        wasted_water += waste

if bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}" )
if cups:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
from collections import deque

firework_effects = deque(map(int, input().split(", ")))
explosive_power = deque(map(int, input().split(", ")))

dct = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
successfully = False


while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    firework = firework_effects.popleft()
    power = explosive_power.pop()
    result = firework + power

    if result % 3 == 0 and not result % 5 == 0:
        dct["Palm Fireworks"] += 1
    elif result % 5 == 0 and not result % 3 == 0:
        dct["Willow Fireworks"] += 1
    elif result % 5 == 0 and result % 3 == 0:
        dct["Crossette Fireworks"] += 1
    else:
        firework -= 1
        firework_effects.append(firework)
        explosive_power.append(power)

    if dct["Palm Fireworks"] >= 3 and dct["Willow Fireworks"] >= 3 and dct["Crossette Fireworks"] >= 3:
        successfully = True
        break

if successfully:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for key, value in dct.items():
    print(f"{key}: {value}")
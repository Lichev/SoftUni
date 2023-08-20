from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque(int(s) for s in input().split(", "))

milkshakes = 0

while True:
    if milkshakes >= 5:
        break

    if not chocolate:
        break

    if not milk:
        break

    valid = False

    first_milk = milk[0]
    last_chocolate = chocolate[-1]

    if first_milk <= 0:
        milk.popleft()
        valid = True

    if chocolate[-1] <= 0:
        chocolate.pop()
        valid = True
        
    if valid:
        continue
    
    if first_milk == last_chocolate:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        if milk and chocolate:
            milk.append(milk.popleft())
            chocolate[-1] -= 5


if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolate:
    print(f'Chocolate: {", ".join(map(str, chocolate))}')
else:
    print(f'Chocolate: empty')

if milk:
    print(f'Milk: {", ".join(map(str, milk))}')
else:
    print(f"Milk: empty")
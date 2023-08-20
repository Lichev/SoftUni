from collections import deque

orders = deque(map(int, input().split(", ")))
employees = deque(map(int, input().split(", ")))

total_pizza = 0

while orders and employees:
    if orders[0] <= 0:
        orders.popleft()
        continue
    elif orders[0] > 10:
        orders.popleft()
        continue

    pizza = orders.popleft()
    employeer = employees.pop()

    if pizza <= employeer:
        total_pizza += pizza
    else:
        pizza -= employeer
        orders.appendleft(pizza)
        total_pizza += employeer

if not orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    if employees:
        print(f"Employees: {', '.join(map(str, employees))}")


else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")

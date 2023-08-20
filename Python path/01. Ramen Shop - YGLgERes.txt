from collections import deque

bowls_of_ramen = deque(input().split(", "))
customers = deque(input().split(", "))

while bowls_of_ramen and customers:
    bowl = int(bowls_of_ramen.pop())
    current_customer = int(customers.popleft())

    if bowl == current_customer:
        continue
    elif bowl > current_customer:
        bowl -= current_customer
        bowls_of_ramen.append(bowl)
    else:
        current_customer -= bowl
        customers.appendleft(current_customer)


if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls_of_ramen))}')
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(map(str, customers))}')

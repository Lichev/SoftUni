from collections import deque


def max_o(ord):
    max_num = 0
    while ord:
        current = ord.pop()
        if current > max_num:
            max_num = current
    return max_num


available = int(input())
orders = deque(int(x) for x in input().split())

neshto = list(orders)
max_order = max_o(neshto)

print(max_order)
while orders:

    current_order = orders[0]

    if current_order <= available:
        available -= current_order
        orders.popleft()
    else:
        print(f'Orders left: {" ".join(map(str, orders))}')
        break

if not orders:
    print(f'Orders complete')
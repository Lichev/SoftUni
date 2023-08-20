from collections import deque

price_bullet = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(l) for l in input().split()]
value_of_intelligence = int(input())

queue_of_locks = deque(locks)
money_for_bullets = 0
shooted_bullets = 0

while True:
    if not bullets:
        break
    if not queue_of_locks:
        if shooted_bullets == barrel:
            print(f'Reloading!')
        break

    if shooted_bullets == barrel:
        print(f'Reloading!')
        shooted_bullets = 0
    current_bullet = bullets.pop()
    money_for_bullets += price_bullet

    if current_bullet > queue_of_locks[0]:
        print('Ping!')
    else:
        queue_of_locks.popleft()
        print(f'Bang!')


    shooted_bullets += 1

if not queue_of_locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - money_for_bullets}")
else:
    print(f"Couldn't get through. Locks left: {len(queue_of_locks)}")

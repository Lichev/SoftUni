walks = input()

steps = 0
last = 0

while steps < 10000:

    if walks == "Going home":
        last_one = input()
        b = int(last_one)
        steps += b
        break

    k = int(walks)
    steps += k

    if steps > 10000:
        break

    walks = input()

diff = abs(steps - 10000)

if steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')

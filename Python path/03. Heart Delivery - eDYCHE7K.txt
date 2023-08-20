houses = [int(x) for x in input().split("@")]

jump = 0

while True:
    command = input()

    if command == 'Love!':
        print(f"Cupid's last position was {jump}.")
        break

    data = command.split(" ")
    how_far = int(data[1])
    jump += how_far
    if jump >= len(houses):
        jump = 0
    if houses[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
        continue
    houses[jump] -= 2
    if houses[jump] == 0:
        print(f"Place {jump} has Valentine's day.")

count_houses = list(filter(lambda number: number > 0, houses))

if sum(houses) == 0:
    print(f'Mission was successful.')
else:
    print(f"Cupid has failed {len(count_houses)} places.")

from collections import deque

free_seats = input().split(", ")
first = deque(int(x) for x in input().split(", "))
second = deque(int(s) for s in input().split(", "))
seat_matches = 0
rotations_count = 0
taken_seats = []

while True:
    if seat_matches >= 3 or rotations_count >= 10:
        break

    first_number = first.popleft()
    second_number = second.pop()
    result = chr(first_number + second_number)
    seats = [str(first_number) + result, str(second_number) + result]

    for n in free_seats:
        if seats[0] == n and seats[0] not in taken_seats:
            taken_seats.append(n)
            to_remove = n
            seat_matches += 1
            break
        elif seats[1] == n and seats[1] not in taken_seats:
            taken_seats.append(n)
            to_remove = n
            seat_matches += 1
            break
    else:
        first.append(first_number)
        second.appendleft(second_number)
    rotations_count += 1

print(f'Seat matches: {", ".join(map(str, taken_seats))}')
print(f'Rotations count: {rotations_count}')


from collections import deque

durutation = int(input())
window = int(input())

cars = deque()
passed_cars = 0
green_ligt = durutation
free_window = window
crash = False

while True:
    command = input()
    green_ligt = durutation
    free_window = window

    if command == 'END':
        break

    if command != 'green':
        cars.append(command)
    else:
        while green_ligt > 0:
            if not cars:
                break
            first = len(cars[0])
            car = cars[0]
            if green_ligt > 0:

                if green_ligt + free_window < first:
                    index = first - (green_ligt + free_window)
                    print(f'A crash happened!')
                    print(f'{car} was hit at {car[-index]}.')
                    crash = True
                    break
                else:
                    green_ligt -= first
                    cars.popleft()
                    passed_cars += 1
    if crash:
        break


if not crash:
    print(f'Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')
def drive(cars, car, distance, fuel):
    if cars[car]['fuel'] < fuel:
        print(f'Not enough fuel to make that ride')
    else:
        cars[car]['distance'] += distance
        cars[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if cars[car]['distance'] >= 100000:
        print(f"Time to sell the {car}!")
        del cars[car]

    return cars


def refuel(cars, car, fuel):
    needed_fuel = 75 - cars[car]['fuel']
    if fuel > needed_fuel:
        cars[car]['fuel'] += needed_fuel
        print(f'{car} refueled with {needed_fuel} liters')
    else:
        cars[car]['fuel'] += fuel
        print(f'{car} refueled with {fuel} liters')

    return cars


def revert(cars, car, kilometers):
    cars[car]['distance'] -= kilometers
    if cars[car]['distance'] > 10000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        cars[car]['distance'] = 10000

    return cars


number_of_cars = int(input())
cars = {}

for i in range(number_of_cars):
    data = input().split("|")
    car = data[0]
    distance = int(data[1])
    fuel = int(data[2])

    cars[car] = {}
    cars[car]['distance'] = distance
    cars[car]['fuel'] = fuel


command = input()

while command != 'Stop':
    command = command.split(" : ")
    action = command[0]

    if action == 'Drive':
        drive_car = command[1]
        drive_distance = int(command[2])
        drive_fuel = int(command[3])
        cars = drive(cars, drive_car, drive_distance, drive_fuel)

    elif action == 'Refuel':
        refuel_car = command[1]
        refuel_fuel = int(command[2])
        cars = refuel(cars, refuel_car, refuel_fuel)

    elif action == 'Revert':
        revert_car = command[1]
        revert_kilometers = int(command[2])
        cars = revert(cars, revert_car, revert_kilometers)

    command = input()

for primary in cars.keys():
    print(f"{primary} -> ", end='')
    for key, value in cars[primary].items():
        if key == 'distance':
            print(f'Mileage: {value} kms, ', end='')
        else:
            print(f'Fuel in the tank: {value} lt.', end='')
    print()

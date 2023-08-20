num = int(input())

water_tank = 255
liters_tank = 0

for i in range(num):
    pour = int(input())
    if water_tank - pour < 0:
        print(f'Insufficient capacity!')
        continue

    water_tank -= pour
    liters_tank += pour

print(liters_tank)
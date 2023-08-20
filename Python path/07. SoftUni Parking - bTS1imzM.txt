number = int(input())
my_dict = {}

for i in range(number):
    plates = input().split(" ")
    action = plates[0]
    name = plates[1]

    if action == 'register':
        plate_number = plates[2]
        if name not in my_dict.keys():
            my_dict[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif action == 'unregister':
        if name in my_dict.keys():
            del my_dict[name]
            print(f'{name} unregistered successfully')
        else:
            print(f"ERROR: user {name} not found")

[print(f'{key} => {value}') for key, value in my_dict.items()]
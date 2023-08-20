filling = input()

islands_info = {}

while filling != 'Sail':
    filling = filling.split("||")
    island = filling[0]
    population = int(filling[1])
    gold = int(filling[2])

    if island not in islands_info:
        islands_info[island] = {}
        islands_info[island]['population'] = population
        islands_info[island]['gold'] = gold
    else:
        islands_info[island]['population'] += population
        islands_info[island]['gold'] += gold

    filling = input()

events = input()

while events != 'End':
    events = events.split("=>")
    action = events[0]

    if action == 'Plunder':
        town = events[1]
        killed_people = int(events[2])
        stolen_gold = int(events[3])

        if town in islands_info:
            islands_info[town]['population'] -= killed_people
            islands_info[town]['gold'] -= stolen_gold
            print(f"{town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")

            if islands_info[town]['population'] == 0 or islands_info[town]['gold'] == 0:
                del islands_info[town]
                print(f"{town} has been wiped off the map!")

    elif action == 'Prosper':
        prosper_town = events[1]
        prosper_gold = int(events[2])

        if prosper_gold > 0:
            islands_info[prosper_town]['gold'] += prosper_gold
            print(f"{prosper_gold} gold added to the city treasury. {prosper_town} now has {islands_info[prosper_town]['gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    events = input()


if len(islands_info) > 0:
    print(f"Ahoy, Captain! There are {len(islands_info)} wealthy settlements to go to:")
    [print(f"{towns} -> Population: {islands_info[towns]['population']} citizens, Gold: {islands_info[towns]['gold']} kg") for towns in islands_info]
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


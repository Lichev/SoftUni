from collections import defaultdict

command = input()

mydict = defaultdict(list)

while command != "Lumpawaroo":

    if "|" in command:
        data = command.split(" | ")
        side = data[0]
        name = data[1]
        validation = False
        if side not in mydict.keys():
            mydict[side] = []

        for key, value in mydict.items():
            if name in value:
                validation = True

        if not validation:
            mydict[side].append(name)


    elif "->" in command:
        data = command.split(" -> ")
        user = data[0]
        side = data[1]

        if side not in mydict.keys():
            mydict[side] = []
            mydict[side].append(user)
        else:
            for key, value in mydict.items():
                for i in value:
                    if i == user:
                        value.remove(i)
            mydict[side].append(user)
        print(f'{user} joins the {side} side!')

    command = input()

for key, value in mydict.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        [print(f"! {i}") for i in value]

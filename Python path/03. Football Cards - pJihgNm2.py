vhod = input()

mylist = vhod.split(" ")
mylist = list(dict.fromkeys(mylist))

a_team = 11
b_team = 11

for i in mylist:
    if "A" in i:
        a_team -= 1
    if "B" in i:
        b_team -= 1


print(f"Team A - {a_team}; Team B - {b_team}")

if a_team < 7 or b_team < 7:
    print(f"Game was terminated")
numbers = input()

bufer = numbers.split(" ")
map_object = map(int,bufer)
listofint = list(map_object)
new_list = list()

for i in listofint:
    if i >= 1:
        new_list.append(-i)
    else:
        new_list.append(abs(i))

print(new_list)

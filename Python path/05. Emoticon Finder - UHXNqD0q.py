text = input()

mylist = []

for index, value in enumerate(text):
    if value == ':':
        temp = value + text[index + 1]
        mylist.append(temp)

print("\n".join(mylist))
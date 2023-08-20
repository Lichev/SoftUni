text = input()

my_list = []
previous = ""

for i in text:

    if i != previous:
        my_list.append(i)

    previous = i

print("".join(my_list))
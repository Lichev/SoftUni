text = input()

new_list= []
for i in range(len(text)):
    valid = text[i].isupper()

    if valid:
        new_list.append(i)

print(new_list)
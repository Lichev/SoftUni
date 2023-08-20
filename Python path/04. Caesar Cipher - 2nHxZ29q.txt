code = input()
mylist = []
for i in code:
    number = ord(i) + 3
    sign = chr(number)
    mylist.append(sign)

print("".join(mylist))
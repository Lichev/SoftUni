text = input().split(" ")
for x in text:
    temp_list1 = []
    temp_list2 = []
    list1 = []
    list2 = []
    neshto = 0
    for c in x:
        if c.isdigit():
            temp_list1.append(c)
        elif c.isalpha():
            temp_list2.append(c)
        a = "".join(temp_list1)

        chars = int(a)
        neshto = chars

    temp_list2[0], temp_list2[-1] = temp_list2[-1], temp_list2[0]
    list1.append(chr(neshto))
    final = list(list1 + temp_list2)
    print("".join(final), end=' ')
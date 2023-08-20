number = input().split(", ")

list_zeros = list()
normal = list()


for num in number:

    if num == "0":
        list_zeros.append(int(num))
    else:
        normal.append(int(num))


print(f'{normal + list_zeros}')
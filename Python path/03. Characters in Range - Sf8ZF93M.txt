def fuckoff(a, b):
    new_list = []
    begins = ord(a)
    to = ord(b)

    for i in range(begins + 1, to):
        new_list.append(chr(i))

    print(*new_list, sep=" ")


in1 = input()
in2 = input()
fuckoff(in1, in2)

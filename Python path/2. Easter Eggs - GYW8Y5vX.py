n = int(input())

num = n
for r in range(n):
    lst = []
    empty = n - num
    for f in range(1,num):
        lst.append(f)
    for s in range(num, 0, -1):
        lst.append(s)
    num -= 1
    print(" " * empty + "".join(map(str, lst)))
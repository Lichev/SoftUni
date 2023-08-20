n = [int(x) for x in input().split()]

for i in range(len(n)):
    last = n.pop()

    print(last, end=" ")

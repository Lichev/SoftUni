def maximum_multiply(divisor, boundary):

    num = 0

    for i in range(boundary, 0, -1):
        if i % divisor == 0:
            num = i
            break
    return num


n1 = int(input())
n2 = int(input())
print(maximum_multiply(n1, n2))


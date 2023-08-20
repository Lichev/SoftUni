n = int(input())

even = set()
odd = set()

for i in range(1, n+1):
    name = input()

    name_number = [ord(i) for i in name]
    name_number = int(sum(name_number) / i)

    if name_number % 2 == 0:
        even.add(name_number)
    else:
        odd.add(name_number)


if sum(even) == sum(odd):
    u = even.union(odd)
    print(", ".join(map(str, u)))
elif sum(odd) > sum(even):
    d = odd.difference(even)
    print(", ".join(map(str, d)))
elif sum(odd) < sum(even):
    sd = even.symmetric_difference(odd)
    print(", ".join(map(str, sd)))
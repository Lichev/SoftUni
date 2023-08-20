n = int(input())

s = set()

for i in range(n):
    c = input().split()

    for i in c:
        s.add(i)

print("\n".join(s))



# With one iter

n = int(input())

table = set()

for i in range(n):
    new_set = set(i for i in input().split())

    table = table.union(new_set)

print('\n'.join(table))
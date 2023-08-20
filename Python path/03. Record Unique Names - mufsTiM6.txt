n = int(input())

s = set()

for i in range(n):
    name = input()
    s.add(name)


print("\n".join(s))
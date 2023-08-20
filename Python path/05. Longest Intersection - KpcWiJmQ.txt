# 1st with if check
n = int(input())

start = 0
end = 0

s = set()

for i in range(n):
    a, b = input().split("-")
    first = a.split(",")
    second = b.split(",")

    first_a = int(first[0])
    first_b = int(first[1])
    second_a = int(second[0])
    second_b = int(second[1])

    if first_a > second_a:
        start = first_a
    else:
        start = second_a
    if first_b > second_b:
        end = second_b
    else:
        end = first_b

    result = {i for i in range(start, end + 1)}
    s.add(frozenset(result))


final = max(s, key=len)

print(f"Longest intersection is [{', '.join(map(str, final))}] with length {len(final)}")


# 2nd with the intersection 

n = int(input())

start = 0
end = 0

s = set()

for i in range(n):
    a, b = input().split("-")
    first = a.split(",")
    second = b.split(",")

    first_a = int(first[0])
    first_b = int(first[1])
    second_a = int(second[0])
    second_b = int(second[1])

    first_set = {i for i in range(first_a, first_b + 1)}
    second_set = {x for x in range(second_a, second_b + 1)}
    inter = first_set.intersection(second_set)

    if len(inter) > len(s):
        s = inter

print(f"Longest intersection is [{', '.join(map(str, s))}] with length {len(s)}")

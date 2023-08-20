first = set(int(x) for x in input().split())
second = set(int(s) for s in input().split())

n = int(input())
check = False

for _ in range(n):
    data = input().split()
    action = data[0]

    if action == 'Add':
        where = data[1]
        nums = set(int(x) for x in data if x.isdigit())

        if where == 'First':
            first = first.union(nums)
        else:
            second = second.union(nums)

    elif action == 'Remove':
        where = data[1]
        nums = set(int(x) for x in data if x.isdigit())

        if where == 'First':
            first = first.difference(nums)
        else:
            second = second.difference(nums)

    else:
        check = first.issubset(second) or second.issubset(first)
        print(check)
        check = False


print(', '.join(map(str, sorted(first))))
print(', '.join(map(str, sorted(second))))

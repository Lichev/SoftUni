start = int(input())
end = int(input())

list = []

for i in range(start, end + 1):
    list.append(chr(i))

print(*list, sep=' ')
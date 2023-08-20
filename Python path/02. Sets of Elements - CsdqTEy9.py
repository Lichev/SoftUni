## Long

n, m = input().split()

first = set()
second = set()

for i in range(int(n)):
    numbers = int(input())

    first.add(numbers)

for x in range(int(m)):
    num = int(input())

    second.add(num)

c = first.intersection(second)

print("\n".join(map(str, c)))



# Short 

numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])

first = {int(input()) for i in range(n)}
second = {int(input()) for x in range(m)}

print('\n'.join(map(str, first.intersection(second))))



#Middle
n, m = map(int, input().split())

first = set()
second = set()

for i in range(n+m):
    numbers = int(input())
    if i < n:
        first.add(numbers)
    else:
        second.add(numbers)

new = first.intersection(second)

print('\n'.join(map(str, new)))
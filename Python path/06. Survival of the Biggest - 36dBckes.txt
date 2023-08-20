numbers = [int(num) for num in input().split(" ")]
remove = int(input())

for i in range(remove):
    numbers.remove(min(numbers))

print(*numbers, sep=', ')

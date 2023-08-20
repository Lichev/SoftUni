import sys

n = int(input())

max_num = -sys.maxsize
sum_num = 0

for i in range(n):
    numbers = int(input())

    if numbers > max_num:
        max_num = numbers
    sum_num += numbers

result = sum_num - max_num

diff = abs(result - max_num)

if max_num == result:
    print(f'Yes')
    print(f'Sum = {result}')
else:
    print("No")
    print(f'Diff = {diff}')
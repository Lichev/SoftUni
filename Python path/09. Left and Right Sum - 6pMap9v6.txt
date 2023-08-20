n = int(input())

left = 0
right = 0

for i in range(2 * n):
    current_number = int(input())

    if i < n:
        left += current_number
    else:
        right += current_number

diff = abs(left - right)

if left == right:
    print(f'Yes, sum = {left}')
else:
    print(f'No, diff = {diff}')


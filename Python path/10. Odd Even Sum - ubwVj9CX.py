n = int(input())

odd = 0
even = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even += number
    else:
        odd += number


diff = abs(odd - even)

if even == odd:
    print('Yes')
    print(f'Sum = {odd}')
else:
    print('No')
    print(f'Diff = {diff}')


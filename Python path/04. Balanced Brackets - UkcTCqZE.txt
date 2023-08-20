number = int(input())

count_open = 0
count_close = 0

for i in range(number):
    chars = input()

    if '(' in chars:
        count_open += 1

    elif ')' in chars:
        count_close += 1

if count_open == count_close:
    print('BALANCED')
else:
    print(f'UNBALANCED')
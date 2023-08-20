n = int(input())

for i in range(n):
    sign = input()

    if ',' in sign or '.' in sign or '_' in sign:
        print(f'{sign} is not pure!')
    else:
        print(f'{sign} is pure.')
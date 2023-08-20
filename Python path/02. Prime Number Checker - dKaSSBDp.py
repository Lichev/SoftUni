num = int(input())

tag = False

for i in range(2, num):
    if num % i == 0:
        tag = True
        break

if tag:
    print(f'False')
else:
    print(f'True')
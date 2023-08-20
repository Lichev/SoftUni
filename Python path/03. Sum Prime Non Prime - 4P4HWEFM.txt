tag = False
prime = 0
non_prime = 0

while True:
    index = input()

    if index == 'stop':
        break

    index = int(index)

    if index < 0:
        print('Number is negative.')
    else:
        if index > 1:
            for i in range(2, index):
                if index % i == 0:
                    tag = True
                    break
            if tag:
                non_prime += index
                tag = False
            else:
                prime += index

print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {non_prime}')

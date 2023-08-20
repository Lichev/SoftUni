number = int(input())

usernames = set()

for i in range(number):
    name = input()

    usernames.add(name)

print('\n'.join(usernames))
from collections import deque

vowels = deque(input().split())
consonants = input().split()

passed = []

dct = {
    "rose": 0,
    "tulip": 0,
    "lotus": 0,
    "daffodil": 0
}


founded_world = ''
found = False

while vowels and consonants:
    cur_vow = vowels.popleft()
    cur_cons = consonants.pop()


    for key , value in dct.items():
        if cur_vow not in passed:
            dct[key] += key.count(cur_vow)

        if cur_cons not in passed:
            dct[key] += key.count(cur_cons)

        if len(key) == dct[key]:
            founded_world = key
            found = True
            break

    if found:
        break
    passed.append(cur_vow)
    passed.append(cur_cons)


if found:
    print(f"Word found: {founded_world}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
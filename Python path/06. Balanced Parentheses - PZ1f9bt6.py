text = input()

s = []


for i in text:

    if i == '{':
        s.append(1)
    elif i == '(':
        s.append(2)
    elif i == '[':
        s.append(3)

    if s:
        if i == '}':
            if s[-1] == 1:
                s.pop()
        if i == ')':
            if s[-1] == 2:
                s.pop()
        if i == ']':
            if s[-1] == 3:
                s.pop()
    else:
        s.append(4)

if s:
    print(f'NO')
else:
    print(f'YES')
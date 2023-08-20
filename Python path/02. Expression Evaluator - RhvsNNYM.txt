import math
from collections import deque

expression = input().split()

numbers = deque()

for i in expression:
    lst = list()
    result = 0
    if i.lstrip('-').isdigit():
        numbers.append(int(i))

    else:
        while numbers:
            lst.append(numbers.popleft())

        for s in range(len(lst)):
            if s == 0:
                result = lst[s]
            else:
                if i == '*':
                    result *= lst[s]
                elif i == '+':
                    result += lst[s]
                elif i == '-':
                    result -= lst[s]
                elif i == '/':
                    result /= lst[s]

        numbers.append(math.floor(result))

print(sum(numbers))
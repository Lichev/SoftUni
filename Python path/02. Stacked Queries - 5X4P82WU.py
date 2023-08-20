import sys


def min(st):
    min_num = sys.maxsize

    for i in range(len(st)):
        current = st.pop()

        if current < min_num:
            min_num = current

    return min_num

def max(st):
    max_num = 0

    for i in range(len(st)):
        current = st.pop()

        if current > max_num:
            max_num = current

    return max_num


n = int(input())

stack = []

for i in range(n):
    command = input().split()
    action = command[0]

    temp = list(stack)
    if action == '1':
        number = int(command[1])
        stack.append(number)

    elif action == '2':
        if stack:
            stack.pop()

    elif action == '3':
        print(max(temp))

    elif action == '4':
        print(min(temp))


new = []
while stack:
    current = stack.pop()
    new.append(str(current))

print(', '.join(new))
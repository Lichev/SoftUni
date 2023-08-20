from collections import deque


def find_the_result(nums):
    lst = deque(nums)
    cycles = len(lst)
    new_list = []

    for i in range(cycles):
        current_num = lst.popleft()
        result = 1
        for n in lst:
            result = result * n

        lst.append(current_num)
        new_list.append(result)
    return sum(new_list)

dct = {}
while True:
    name = input()
    if name == 'stop':
        break
    nums = list(map(int, input().split(", ")))

    if name not in dct:
        dct[name] = 0

    dct[name] += find_the_result(nums)


[print(f'{key} has a bonus of {value} lv.') for key, value in dct.items()]
print(f'The amount of all bonuses is {sum(dct.values())} lv.')
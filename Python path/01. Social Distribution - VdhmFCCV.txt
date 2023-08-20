n = [int(i) for i in input().split(", ")]
minimum = int(input())


def wealthiest(numbers):
    maxs = max(numbers)
    ind = 0
    for index, x in enumerate(numbers):
        if x == maxs:
            ind = index
    return ind


def not_possible(numbers, minimums):
    for index1, i in enumerate(n):
        if i < minimum:
            return True



for index, i in enumerate(n):
    if i < minimum:
        add = minimum - i
        max_index = wealthiest(n)
        n[index] += add
        n[max_index] -= add

validation = not_possible(n, minimum)

if validation:
    print(f'No equal distribution possible')
else:
    print(n)
      
      
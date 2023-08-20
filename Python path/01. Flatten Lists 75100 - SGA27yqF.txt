# 75/100

text = input().split("|")

list_of_nums = []

for x in text:
    list_of_nums.extend([x.split()])

rever = list(reversed(list_of_nums))

[print(*x, end=' ') for x in rever]

text = input().split("|")

list_of_nums = []

for x in text[::-1]:
    list_of_nums.extend(x.split())



print(*list_of_nums, end=" ")
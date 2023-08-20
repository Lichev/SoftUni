numbers = [int(n) for n in input().split(" ")]

avarege = sum(numbers) / len(numbers)

count = 0
new_list = []

numbers = sorted(numbers, reverse=True)

for i in numbers:
    if i > avarege:
        new_list.append(i)
        count += 1
        if count >= 5:
            break

if len(new_list) == 0:
    print(f'No')
else:
    print(" ".join(map(str, sorted(new_list, reverse=True))))

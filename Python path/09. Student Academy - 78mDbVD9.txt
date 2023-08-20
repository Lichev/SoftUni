from collections import defaultdict

number = int(input())

my_dict = defaultdict(list)

for i in range(number):
    name = input()
    grade = float(input())

    if name not in my_dict.keys():
        my_dict[name] = []

    my_dict[name].append(grade)


for key, value in my_dict.items():
    if (sum(value) / len(value)) >= 4.50:
        print(f'{key} -> {sum(value) / len(value):.2f}')
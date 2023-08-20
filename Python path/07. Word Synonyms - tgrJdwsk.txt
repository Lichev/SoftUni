from collections import defaultdict

number = int(input())

my_list = defaultdict(list)

for i in range(number):
    word, synonym = input(), input()

    my_list[word].append(synonym)


for key, value in my_list.items():
    print(f'{key} - {", ".join(value)}')
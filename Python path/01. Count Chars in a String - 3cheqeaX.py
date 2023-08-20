text = input()

my_dict = {}


for char in text:

    if char == ' ':
        continue

    if char not in my_dict:
        my_dict[char] = 1
    else:
        my_dict[char] += 1


for key, value in my_dict.items():
    print(f'{key} -> {value}')
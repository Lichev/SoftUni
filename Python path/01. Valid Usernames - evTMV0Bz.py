text = input().split(", ")

my_list = []
fist_validation = False
second_validation = True
third_validation = True

special_char = ['[', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', "\\", '|', '}', '{', '~',
                ':', ']']

for word in text:

    if 3 <= len(word) <= 16:
        fist_validation = True

    for i in special_char:
        if i in word:
            second_validation = False
            break
    if " " in word:
        third_validation = False

    if fist_validation and second_validation and third_validation:
        my_list.append(word)

    fist_validation = False
    second_validation = True
    third_validation = True

print("\n".join(my_list))

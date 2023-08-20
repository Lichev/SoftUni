text = [text.strip() for text in input().split(" ") if text != ""]

total = 0

for i in text:
    temp_total = 0
    first_l = i[0]
    second_l = i[-1]
    number = i[1:len(i) - 1]

    first_index = ord(first_l.lower()) - 96
    second_index = ord(second_l.lower()) - 96

    if first_l.islower():
        temp_total = (int(number) * first_index)
    else:
        temp_total = (int(number) / first_index)

    if second_l.islower():
        temp_total = temp_total + second_index
    else:
        temp_total = temp_total - second_index

    total += temp_total

print(f"{total:.2f}")

text = input()

unique = []
new_text = ''

txt_temp = ''
num_temp = ''
for i in range(len(text)):
    validation = text[i].isnumeric()
    if validation:
        num_temp += text[i]

        if i + 1 < len(text):
            if text[i + 1].isnumeric():
                continue

        txt_temp = txt_temp.upper()
        new_text += txt_temp * int(num_temp)
        txt_temp = ''
        num_temp = ''
    else:
        txt_temp += text[i]
        if text[i].lower() not in unique:
            unique.append(text[i].lower())

print(f'Unique symbols used: {len(unique)}')
print(new_text)

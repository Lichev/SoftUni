text = input()
stenght = 0
new_text = ''

for index in range(len(text)):
    if stenght > 0 and text[index] != '>':
        stenght -= 1
    elif text[index] == ">":
        stenght += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)
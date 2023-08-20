import re

text = input()

sample = r'#[A-Z\s?a-z]+#\d{2}\/\d{2}\/\d{2}#[0-9]{1,5}#|\|[A-Z\s?a-z]+\|\d{2}\/\d{2}\/\d{2}\|[0-9]{1,5}\|'
matches = re.findall(sample, text)

lst = []

for match in matches:
    lst.append(match)

total_calories = 0
new_list = []

for i in lst:
    if '#' in i:
        data = i.split('#')
    else:
        data = i.split('|')

    data = [x for x in data if x != '']
    new_list.append(data)
    total_calories += int(data[2])

print(f'You have food to last you for: {int(total_calories / 2000)} days! ')
if len(new_list) > 0:
    for current in new_list:
        print(f'Item: {current[0]}, Best before: {current[1]}, Nutrition: {current[2]}')


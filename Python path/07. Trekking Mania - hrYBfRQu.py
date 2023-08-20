number_of_groups = int(input())

all_people = 0
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(number_of_groups):
    people_in_group = int(input())
    all_people += people_in_group

    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        mont_blanc += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

print(f'{(musala / all_people) * 100:.2f}%')
print(f'{(mont_blanc / all_people) * 100:.2f}%')
print(f'{(kilimanjaro / all_people) * 100:.2f}%')
print(f'{(k2 / all_people) * 100:.2f}%')
print(f'{(everest / all_people) * 100:.2f}%')

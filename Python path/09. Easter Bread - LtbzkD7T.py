budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25

for_one_loaves = price_eggs + price_flour + (price_milk / 4)

count_eggs = 0
count_loaves = 0

while budget >= 0:
    if budget < for_one_loaves:
        break
    budget -= for_one_loaves
    count_loaves += 1
    count_eggs += 3

    if count_loaves % 3 == 0:
        count_eggs = count_eggs - (count_loaves - 2)

print(f"You made {count_loaves} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")

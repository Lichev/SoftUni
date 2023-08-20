budget = float(input())
price_for_flour = float(input())

pack_of_eggs = price_for_flour * 0.75
price_for_liter = price_for_flour + (price_for_flour * 0.25)
price_for_250 = price_for_liter / 4
coloured_eggs = 0
loaf = 0


while True:
    price_for_loaf = pack_of_eggs + price_for_flour + price_for_250

    if (budget - price_for_loaf) < 0:
        break

    budget -= price_for_loaf
    loaf += 1
    coloured_eggs += 3

    if loaf % 3 == 0:
        coloured_eggs = coloured_eggs - (loaf - 2)


print(f'You made {loaf} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')
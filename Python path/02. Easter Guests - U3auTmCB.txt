import math

guests = int(input())
budget = int(input())

kozunak = math.ceil(guests / 3)
eggs = guests * 2

priceK = kozunak * 4
priceE = eggs * 0.45
all = priceE + priceK
diff = abs(all - budget)

if budget < all:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')
else:
    print(f'Lyubo bought {kozunak} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')

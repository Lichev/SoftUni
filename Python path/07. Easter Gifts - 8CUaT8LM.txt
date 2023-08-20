product = input().split()
new = len(product)

while True:
    cards = input()

    if cards == 'No Money':
        break

    newlist = cards.split(" ")

    if newlist[0] == 'OutOfStock':
        for index, current_gift in enumerate(product):
            if current_gift == newlist[1]:
                product[index] = 'None'
    elif newlist[0] == 'Required':
        position = int(newlist[2])
        if 0 < position < len(product):
            product[position] = newlist[1]
    elif newlist[0] == 'JustInCase':
        product[-1] = newlist[1]

while 'None' in product:
    product.remove('None')


print(*product, sep=' ')
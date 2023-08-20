def shopping_cart(*args):
    check = {
        'Dessert': 2,
        'Pizza': 4,
        'Soup': 3
    }

    final = {
        'Dessert': [],
        'Pizza': [],
        'Soup': []
    }

    products = 0
    for data in args:
        if data == 'Stop':
            break
        meal = data[0]
        product = data[1]
        if check[meal] > 0:
            if product not in final[meal]:
                final[meal].append(product)
                check[meal] -= 1
                products += 1

    final = dict(sorted(final.items(), key=lambda x: (-len(x[1]), x[0],)))

    for key, value in final.items():
        final[key] = sorted(value, key= lambda x: x)
        pass


    lst = []

    for key, value in final.items():
        lst.append(key + ':')
        for v in value:
            lst.append(" - " + v)

    if products > 0:
        return "\n".join(lst)
    else:
        return f'No products in the cart!'





print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

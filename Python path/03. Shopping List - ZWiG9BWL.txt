def shopping_list(*args, **kwargs):
    budget = args[0]
    number_of_products = 0

    bought_products = []

    if budget >= 100:
        for key, value in kwargs.items():
            price, quantitiy = value[0], value[1]
            total_price = float(price) * int(quantitiy)

            if total_price <= budget:
                budget -= total_price
                bought_products.append(f"You bought {key} for {total_price:.2f} leva.")
                number_of_products += 1
            if number_of_products == 5:
                break
        return '\n'.join(bought_products)
    else:
        return "You do not have enough budget."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

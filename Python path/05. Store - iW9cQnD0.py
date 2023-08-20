name_of_product = input()
city = input()
quantity = float(input())

result = 0

if city == 'Sofia':
    if name_of_product == 'coffee':
        result = quantity * 0.50
    elif name_of_product == 'water':
        result = quantity * 0.80
    elif name_of_product == 'beer':
        result = quantity * 1.20
    elif name_of_product == 'sweets':
        result = quantity * 1.45
    elif name_of_product == 'peanuts':
        result = quantity * 1.60
elif city == 'Plovdiv':
    if name_of_product == 'coffee':
        result = quantity * 0.40
    elif name_of_product == 'water':
        result = quantity * 0.70
    elif name_of_product == 'beer':
        result = quantity * 1.15
    elif name_of_product == 'sweets':
        result = quantity * 1.30
    elif name_of_product == 'peanuts':
        result = quantity * 1.50
elif city == 'Varna':
    if name_of_product == 'coffee':
        result = quantity * 0.45
    elif name_of_product == 'water':
        result = quantity * 0.70
    elif name_of_product == 'beer':
        result = quantity * 1.10
    elif name_of_product == 'sweets':
        result = quantity * 1.35
    elif name_of_product == 'peanuts':
        result = quantity * 1.55

print(result)
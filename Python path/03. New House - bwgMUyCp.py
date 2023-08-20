flowers = input()
number_of_flowers = int(input())
budget = int(input())

discount = 0
result = 0

if flowers == 'Roses':
    result = number_of_flowers * 5
    if number_of_flowers > 80:
        discount = 0.10
        result = result - (result * discount)
elif flowers == 'Dahlias':
    result = number_of_flowers * 3.80
    if number_of_flowers > 90:
        discount = 0.15
        result = result - (result * discount)
elif flowers == 'Tulips':
    result = number_of_flowers * 2.80
    if number_of_flowers > 80:
        discount = 0.15
        result = result - (result * discount)
elif flowers == 'Narcissus':
    result = number_of_flowers * 3
    if number_of_flowers < 120:
        discount = 0.15
        result = result + (result * discount)
elif flowers == 'Gladiolus':
    result = number_of_flowers * 2.50
    if number_of_flowers < 80:
        discount = 0.20
        result = result + (result * discount)

if budget >= result:
    result = budget - result
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers} and {result:.2f} leva left.')
else:
    result = result - budget
    print(f'Not enough money, you need {result:.2f} leva more.')
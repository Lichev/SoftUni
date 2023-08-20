import math

days = int(input())
quantity_of_food = float(input())

total_biscuits = 0
biscuits = 0
food_for_dog = 0
food_for_cat = 0
food_for_the_day = 0

for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    food_for_dog += dog_food
    food_for_cat += cat_food

    if i % 3 == 0:
        total_biscuits = 0.10 * (dog_food + cat_food)
        biscuits += total_biscuits

total_food = food_for_dog + food_for_cat
percent_total = (total_food / quantity_of_food) * 100

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{percent_total:.2f}% of the food has been eaten.')
print(f'{(food_for_dog / total_food) * 100:.2f}% eaten from the dog.')
print(f'{(food_for_cat / total_food) * 100:.2f}% eaten from the cat.')

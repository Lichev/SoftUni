fruit = input()
day_of_week = input()
quantity = float(input())

result = 0

if day_of_week == 'Monday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        print('error')

elif day_of_week == 'Tuesday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        print('error')
elif day_of_week == 'Wednesday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        print('error')
elif day_of_week == 'Thursday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        print('error')
elif day_of_week == 'Friday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        print('error')
elif day_of_week == 'Saturday':
    if fruit == 'banana':
        result = quantity * 2.70
    elif fruit == 'apple':
        result = quantity * 1.25
    elif fruit == 'orange':
        result = quantity * 0.90
    elif fruit == 'grapefruit':
        result = quantity * 1.60
    elif fruit == 'kiwi':
        result = quantity * 3.00
    elif fruit == 'pineapple':
        result = quantity * 5.60
    elif fruit == 'grapes':
        result = quantity * 4.20
    else:
        print('error')
elif day_of_week == 'Sunday':
    if fruit == 'banana':
        result = quantity * 2.70
    elif fruit == 'apple':
        result = quantity * 1.25
    elif fruit == 'orange':
        result = quantity * 0.90
    elif fruit == 'grapefruit':
        result = quantity * 1.60
    elif fruit == 'kiwi':
        result = quantity * 3.00
    elif fruit == 'pineapple':
        result = quantity * 5.60
    elif fruit == 'grapes':
        result = quantity * 4.20
    else:
        print('error')
else:
    print('error')

if result != 0:
    print(f'{result:.2f}')
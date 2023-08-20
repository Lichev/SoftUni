number_of_jamove = int(input())
type_of_jam = input()
type_of_delivery = input()

sum = 0

if number_of_jamove >= 10:
    if type_of_jam == '90X130':
        sum = 110 * number_of_jamove
        if 30 < number_of_jamove < 60:
            sum = sum - (sum * 0.05)
        elif number_of_jamove >= 60:
            sum = sum - (sum * 0.05)
    elif type_of_jam == '100X150':
        sum = 140 * number_of_jamove
        if 40 < number_of_jamove < 80:
            sum = sum - (sum * 0.06)
        elif number_of_jamove >= 80:
            sum = sum - (sum * 0.10)
    elif type_of_jam == '130X180':
        sum = 190 * number_of_jamove
        if 20 < number_of_jamove < 50:
            sum = sum - (sum * 0.07)
        elif number_of_jamove >= 50:
            sum = sum - (sum * 0.12)
    elif type_of_jam == '200X300':
        sum = 250 * number_of_jamove
        if 25 < number_of_jamove < 50:
            sum = sum - (sum * 0.09)
        elif number_of_jamove >= 50:
            sum = sum - (sum * 0.14)

    if type_of_delivery == "With delivery":
        sum += 60
    if number_of_jamove > 99:
        sum = sum - (sum * 0.04)


    print(f"{sum:.2f} BGN")
else:
    print(f'Invalid order')
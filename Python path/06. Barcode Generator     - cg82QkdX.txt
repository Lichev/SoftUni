number_one = input()
number_two = input()

for num1 in range(int(number_one[0]), int(number_two[0]) + 1):
    for num2 in range(int(number_one[1]), int(number_two[1]) + 1):
        for num3 in range(int(number_one[2]), int(number_two[2]) + 1):
            for num4 in range(int(number_one[3]), int(number_two[3]) + 1):

                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0 :

                    print(f'{num1}{num2}{num3}{num4}', end= ' ')

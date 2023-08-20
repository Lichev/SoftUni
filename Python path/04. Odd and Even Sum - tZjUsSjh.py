def odd_even_sum(text):

    odd = 0
    even = 0

    for i in text:
        to_int = int(i)

        if to_int % 2 == 0:
            even += to_int
        else:
            odd += to_int

    print(f'Odd sum = {odd}, Even sum = {even}')


vhod = input()
odd_even_sum(vhod)


def perfect_number(num):
    new_list = []

    for i in range(1, num):
        if num % i == 0:
            new_list.append(i)

    if sum(new_list) == num:
        print(f'We have a perfect number!')
    else:
        print(f"It's not so perfect.")


number = int(input())
perfect_number(number)
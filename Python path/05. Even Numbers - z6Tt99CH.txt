def even_number(numbers):
    new_list = [n for n in numbers if n % 2 == 0]
    return new_list


num = [int(x) for x in input().split(" ")]
print(even_number(num))

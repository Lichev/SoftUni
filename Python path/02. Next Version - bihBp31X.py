numbers = input().split('.')

a = ''.join(numbers)
on_int = int(a) + 1
str_again = str(on_int)

new_list = []

for i in str_again:
    new_list.append(i)

print('.'.join(new_list))

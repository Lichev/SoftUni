def drink(age):
    if age <= 14:
        print(f'drink toddy')
    elif age <= 18:
        print(f'drink coke')
    elif age <= 21:
        print(f'drink beer')
    elif age > 21:
        print(f'drink whisky')


n = int(input())
drink(n)



projection = input()
package = input()
number_of_tickets = int(input())

result = 0

if projection == 'John Wick':
    if package == 'Drink':
        result = number_of_tickets * 12
    elif package == 'Popcorn':
        result = number_of_tickets * 15
    elif package == 'Menu':
        result = number_of_tickets * 19
elif projection == 'Star Wars':
    if package == 'Drink':
        result = number_of_tickets * 18
    elif package == 'Popcorn':
        result = number_of_tickets * 25
    elif package == 'Menu':
        result = number_of_tickets * 30
elif projection == 'Jumanji':
    if package == 'Drink':
        result = number_of_tickets * 9
    elif package == 'Popcorn':
        result = number_of_tickets * 11
    elif package == 'Menu':
        result = number_of_tickets * 14

if projection == 'Star Wars' and number_of_tickets >= 4:
    result = result - (result * 0.30)
elif projection == 'Jumanji' and number_of_tickets == 2:
    result = result - (result * 0.15)

print(f'Your bill is {result:.2f} leva.')

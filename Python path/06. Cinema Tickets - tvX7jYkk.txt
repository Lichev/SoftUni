students = 0
standart = 0
kid = 0
total = 0

while True:
    movie = input()

    if movie == 'Finish':
        break

    seats = int(input())

    temp = 0

    for i in range(seats):
        type_ticket = input()

        if type_ticket == 'End':
            break
        temp += 1
        if type_ticket == 'student':
            students += 1
            total += 1
        elif type_ticket == 'standard':
            standart += 1
            total += 1
        elif type_ticket == 'kid':
            kid += 1
            total += 1
    print(f'{movie} - {(temp / seats) * 100:.2f}% full.')

print(f'Total tickets: {total}')
print(f'{(students / total) * 100:.2f}% student tickets.')
print(f'{(standart / total) * 100:.2f}% standard tickets.')
print(f'{(kid / total) * 100:.2f}% kids tickets.')

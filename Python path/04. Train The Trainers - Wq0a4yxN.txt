n = int(input())

final = 0
count = 0


while True:

    name = input()

    if name == 'Finish':
        print(f"Student's final assessment is {final / count:.2f}.")
        break

    temporary = 0
    for i in range(n):
        score = float(input())
        temporary += score
        count += 1
    middle = temporary / n
    final += temporary
    print(f'{name} - {middle:.2f}.')



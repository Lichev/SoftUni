def sum_cols(matrix , row, col):
    total_points = 0
    for x in range(6):
        if matrix[x][col].isdigit():
            total_points += int(matrix[x][col])
    return total_points


matrix = [input().split() for x in range(6)]

total_points = 0
passed = []

for x in range(3):
    data = input().strip("()").split(", ")

    row = int(data[0])
    col = int(data[1])
    coordinates = [row, col]
    if 0 <= row < 6 and 0 <= col < 6:
        if matrix[row][col] == 'B' and coordinates not in passed:
            total_points += sum_cols(matrix, row, col)
            passed.append(coordinates)

prize = ''

if 100 <= total_points < 200:
    prize = 'Football'
elif 200 <= total_points < 300:
    prize = 'Teddy Bear'
elif total_points >= 300:
    prize = 'Lego Construction Set'

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
def battlefield(number_of_rows):
    field = []

    for i in range(number_of_rows):
        ships = list(map(int, input().split(" ")))
        field.append(ships)

    return field


def general(numbers):
    battle_field = battlefield(numbers)
    attacks = input().split(" ")

    destroyed_ships = 0

    for i in attacks:
        data = i.split("-")
        row = int(data[0])
        columnd = int(data[1])

        for index_row, rows in enumerate(battle_field):
            for index_col, col in enumerate(rows):
                if index_row == row and index_col == columnd and col > 0:
                    rows[index_col] -= 1
                    if rows[index_col] == 0:
                        destroyed_ships += 1
                    break
    return destroyed_ships


number = int(input())
print(general(number))

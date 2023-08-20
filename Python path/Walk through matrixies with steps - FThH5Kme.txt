def walk(matrix, direction, steps, rows, cols):
    santa_row, santa_col = santa_position(matrix, rows, cols) # another functions for the positions of the person
    lst_with_items = []

    if directions == 'right':
        for x in range(int(steps)):
            santa_col += 1
            if santa_col > cols - 1:
                santa_col = 0
            lst_with_items.append([santa_row, santa_col])

    elif directions == 'left':
        for x in range(int(steps)):
            santa_col -= 1
            if santa_col < 0:
                santa_col = cols - 1
            lst_with_items.append([santa_row, santa_col])
    elif directions == 'up':
        for x in range(int(steps)):
            santa_row -= 1
            if santa_row < 0:
                santa_row = rows - 1
            lst_with_items.append([santa_row, santa_col])
    elif directions == 'down':
        for x in range(int(steps)):
            santa_row += 1
            if santa_row > rows - 1:
                santa_row = 0
            lst_with_items.append([santa_row, santa_col])

    return lst_with_items
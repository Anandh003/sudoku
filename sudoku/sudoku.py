import numpy as np
import numpy as np

def check_valid_table(table):
    for row in range(9):
        for column in range(9):
            value = table[row][column]
            if value:
                for t_column in range(column + 1, 9):
                    if value == table[row][t_column]:
                        return False

                for t_row in range(row + 1, 9):
                    if value == table[t_row][column]:
                        return False

                s_box_x_start = (row // 3) * 3
                s_box_y_start = (column // 3) * 3
                s_box_x_end = s_box_x_start + 3
                s_box_y_end = s_box_y_start + 3

                for i in range(s_box_x_start, s_box_x_end):
                    for j in range(s_box_y_start, s_box_y_end):
                        if (
                            table[i][j] and not (i == row and j == column)
                            and table[i][j] == value
                        ):
                            return False

    return True


def all_filled(table):
    for row in range(9):
        for column in range(9):
            if table[row][column] == 0:
                return False
    return True


def print_grid(table):
    print(9 * 2 * 2 * '-')
    for column in range(9):
        for row in table[:][column]:
            print('|', end=' ')
            print(row, end=' ')
        print('|')
        print(9 * 2 * 2 * '-')


def auto_complete(table):
    if check_valid_table(table) and all_filled(table):
        return True

    for row in range(0, 9):
        for column in range(0, 9):
            if table[row][column] == 0:
                for number in range(1, 10):
                    table[row][column] = number
                    if check_valid_table(table):
                        if auto_complete(table):
                            return True
                        else:
                            table[row][column] = 0
                    else:
                        table[row][column] = 0
                return False


table_data = [
    [0, 0, 6, 0, 0, 4, 1, 2, 0],
    [0, 0, 0, 0, 9, 0, 6, 7, 0],
    [0, 0, 0, 0, 2, 0, 5, 0, 3],
    [5, 0, 0, 9, 0, 0, 0, 0, 7],
    [0, 9, 7, 0, 0, 0, 2, 3, 0],
    [1, 0, 0, 0, 0, 2, 0, 0, 4],
    [7, 0, 8, 0, 6, 0, 0, 0, 0],
    [0, 4, 5, 0, 3, 0, 0, 0, 0],
    [0, 6, 9, 2, 0, 0, 4, 0, 0],
]

sudoku_table = np.array(table_data)
# print(check_valid_table(table_data))
auto_complete(table_data)
# print(table_data)
print_grid(table_data)

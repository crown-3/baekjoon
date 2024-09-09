from typing import List

# There cannot be two or more queens in a row.
# However, there exists N rows and N queens.
# Thus, exactly one queen should be placed in each row.
# In the same manner, exactly one queen should be placed in each column.

def main(n: int):
    chess_table = []

    return possible_numbers_for_chess_table(chess_table, n)

def possible_numbers_for_chess_table(chess_table: List[int], n: int) -> int:
    if len(chess_table) == n:
        print(chess_table)
        return 1

    possible_columns = []

    for column in range(0, n):
        if (check_directional(chess_table, column)
                or check_diagonal(chess_table, column)):
            continue

        possible_columns.append(column)


    if len(possible_columns) == 0:
        return 0

    return sum(possible_numbers_for_chess_table(chess_table + [possible_column], n)
               for possible_column in possible_columns)



def check_directional(chess_table: List[int], column: int) -> bool:
    if column in chess_table:
        return True
    return False

def check_diagonal(chess_table: List[int], column: int) -> bool:
    flag = False

    for index in range(0, len(chess_table)):
        diff = len(chess_table) - index
        checking_numbers = [chess_table[index] + diff, chess_table[index] - diff]

        if column in checking_numbers:
            flag = True

    return flag

N = int(input())

print(main(N))
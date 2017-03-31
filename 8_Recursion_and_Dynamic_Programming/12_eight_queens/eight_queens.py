from __future__ import print_function
from collections import defaultdict

count = 0
def eight_queens(col, board):
    global count
    if col == 9:
        for r in range(1, 9):
            for c in range(1, 9):
                if board[r] == c:
                    print('*', end='')
                else:
                    print('-', end='')

            print("\n")
        print('============')
        count += 1
        return

    for row in range(1, 9):
        if board[row] == 0 and check_diagonal(board, row, col):
            #print("{}:{}".format(row, col))
            board[row] = col
            eight_queens(col + 1, board)
            board[row] = 0

def check_diagonal(board, row, col):
    for r, c in board.iteritems():
        if c != 0 and abs(row - r) == abs(col - c):
            return False

    return True

def eight_queens_helper():
    # board: row -> col
    board = defaultdict(int)
    eight_queens(1, board)

eight_queens_helper()
print(count)

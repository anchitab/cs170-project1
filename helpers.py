
#Helper tp find all moves and respective costs. WIll return the board after the move.
from copy import deepcopy


def get_all_moves(board):
    def find_zero():
        zero_index = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    zero_index = (i,j)
                    return zero_index
    row, col = find_zero()
    moves = []

    #Left
    if col != 0:
        new_board = deepcopy(board)
        new_board[row][col-1], new_board[row][col] = board[row][col], board[row][col-1]
        moves.append((new_board, 1))

    #Right
    if col != (len(board[0]) - 1):
        new_board = deepcopy(board)
        new_board[row][col+1], new_board[row][col] = board[row][col], board[row][col+1]
        moves.append((new_board, 1))
    
    # Up
    if row != 0:
        new_board = deepcopy(board)
        new_board[row-1][col], new_board[row][col] = new_board[row][col], new_board[row-1][col]
        moves.append((new_board, 1))
    
    # Down
    if row != (len(board) - 1):
        new_board = deepcopy(board)
        new_board[row+1][col], new_board[row][col] = new_board[row][col], new_board[row+1][col]
        moves.append((new_board, 1))


    return moves

def is_goal_state(board):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal_state

#Helper from example slides [TODO! insert slide deck name]
def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')




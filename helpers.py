from copy import deepcopy

# Helper to find all the possible moves and their costs (returns the board after the move)
def get_all_moves(board):
    def find_zero():
        zero_index = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    zero_index = (i, j)
                    return zero_index
    row, col = find_zero()
    moves = []

    # Left
    if col != 0:
        new_board = deepcopy(board)
        new_board[row][col-1], new_board[row][col] = board[row][col], board[row][col-1]
        moves.append(new_board)
    
    # Right
    if col != (len(board[0]) - 1):
        new_board = deepcopy(board)
        new_board[row][col+1], new_board[row][col] = board[row][col], board[row][col+1]
        moves.append(new_board)
    
    # Up
    if row != 0:
        new_board = deepcopy(board)
        new_board[row-1][col], new_board[row][col] = new_board[row][col], new_board[row-1][col]
        moves.append(new_board)
    
    # Down
    if row != (len(board) - 1):
        new_board = deepcopy(board)
        new_board[row+1][col], new_board[row][col] = new_board[row][col], new_board[row+1][col]
        moves.append(new_board)
    
    return moves

def is_goal_state(board):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal_state

# Helper from example slides
def print_puzzle(puzzle): 
    for i in range(0, 3):
        print(puzzle[i]) 
    print('\n')

def board_to_tuple(board):
    new_board = []
    for row in board:
        new_board.append(tuple(row))
    return tuple(new_board)

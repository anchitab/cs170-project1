from ucs import *
from a_star import *

def main():
    mode = input('Welcome to 8-Puzzle Solver! Enter 1 to use an example puzzle or 2 to enter your own puzzle: \n')
    mode = mode.strip()
    puzzle = get_puzzle(mode)
    run_algorithm(puzzle)

def run_algorithm(puzzle):
    algo = input('Enter the algorithm you\'d like to run. Please enter (1) for '
    'Uniform Cost Search, (2) for A* with Misplaced Tile Heuristic, or (3) for '
    'A* with Manhattan heuristic: ')
    algo = int(algo.strip())
    if algo == 1:
        ucs(puzzle)
    elif algo == 2:
        a_star(puzzle, misplaced_heuristic)
    elif algo == 3:
        a_star(puzzle, manhattan_heuristic)
    else:
        print('Error')

def get_puzzle(mode):
    if mode == '1':
        difficulty = input('Enter difficulty (on a scale of 1-5) for your example puzzle: ')
        difficulty = int(difficulty.strip())
        if difficulty == 1:
            print('Depth 2 puzzle selected')
            return depth_2_test
        elif difficulty == 2:
            print('Depth 4 puzzle selected')
            return depth_4_test
        elif difficulty == 3:
            print('Depth 8 puzzle selected')
            return depth_8_test
        elif difficulty == 4:
            print('Depth 12 puzzle selected')
            return depth_12_test
        elif difficulty == 5:
            print('Depth 24 puzzle selected')
            return depth_24_test
        else:
            print('Error')
            return None
    else:
        print('Please enter your valid 8-puzzle space separated using a 0 to represent blank space')
        rows = []
        rows.append(input('Enter your first row (space separated): '))
        rows.append(input('Enter your second row (space separated): '))
        rows.append(input('Enter your third row (space separated): '))

        for i in range(len(rows)):
            new_row = []
            for num in rows[i].strip().split():
                new_row.append(int(num))
            rows[i] = new_row
        return rows




depth_2_test = [
    [1, 2, 3],
    [4, 5, 6], 
    [0, 7, 8]
]
depth_4_test = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]

depth_8_test = [
    [1, 3, 6], 
    [5, 0, 2],
    [4, 7, 8]
]

depth_12_test = [
    [1, 3, 6],
    [5, 0, 7],
    [4, 8, 2]
]
depth_24_test = [
    [0, 7, 2],
    [4, 6, 1],
    [3, 5, 8]
] 

if __name__ == '__main__':
    main()


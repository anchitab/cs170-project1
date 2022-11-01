import time
from ucs import *
from a_star import *

depth_0_test = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 0]
]
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

depth_16_test = [
    [1, 6, 7],
    [5, 0, 3],
    [4, 8, 2]
]

depth_20_test = [
    [7, 1, 2],
    [4, 8, 5],
    [6, 3, 0]
]

depth_24_test = [
    [0, 7, 2],
    [4, 6, 1],
    [3, 5, 8]
]


# Time each algorithm
ucs_times = []
tests = [depth_0_test, depth_2_test, depth_4_test, depth_8_test, depth_12_test, depth_16_test, depth_20_test, depth_24_test]

for puzzle in tests:
    start = time.time()
    ucs(puzzle, timing=True)
    end = time.time()

    ucs_times.append(end-start)

a_star_misplaced_times = []
for puzzle in tests:
    start = time.time()
    a_star(puzzle, misplaced_heuristic, timing=True)
    end = time.time()

    a_star_misplaced_times.append(end-start)

a_star_manhattan_times = []
for puzzle in tests:
    start = time.time()
    a_star(puzzle, manhattan_heuristic, timing=True)
    end = time.time()

    a_star_manhattan_times.append(end-start)

print('UCS Times: ' + str(ucs_times))
print('A* Times (Misplaced Heuristic): ' + str(a_star_misplaced_times))
print('A* Times (Manhattan Heuristic): ' + str(a_star_manhattan_times))
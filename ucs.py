from collections import deque
from helpers import *
from node import Node
import time

def ucs(board, heuristic=None):
    nodes_expanded = 0
    queue = deque()
    start_node = Node(board)
    queue.append((start_node, 0))
    max_size = 1

    seen = set()
    while True:
        if not queue:
            return None
        max_size = max(max_size, len(queue))
        node, depth = queue.popleft()
        nodes_expanded += 1

        if is_goal_state(node.board):
            node.printPath()
            print(f'Solution depth: {depth}')
            print(f'Nodes expanded: {nodes_expanded}')
            print(f'Max queue size: {max_size}')
            return (node.board, depth)
        
        for new_board in get_all_moves(node.board):
            node_tuple = board_to_tuple(new_board)
            if node_tuple not in seen:
                new_node = Node(new_board, prev=node)
                queue.append((new_node, depth + 1))
                seen.add(node_tuple)

right_corner_zero = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

# Examples from project slides
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]] 
oh_boy = [[8, 7, 1],
[6, 0, 2], [5, 4, 3]]

depth_4_test = [
    [1, 2, 3],
    [5, 0, 6],
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

# start = time.time()
# ucs(depth_24_test)
# end = time.time()

# print(f'ELAPSED TIME: {end-start}')
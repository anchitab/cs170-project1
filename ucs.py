from collections import deque
from helpers import *
from node import Node

def ucs(board):
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
        if is_goal_state(node.board):
            node.printPath()
            return (node.board, depth)

        for new_board, cost in get_all_moves(node.board):
            node_tuple = board_to_tuple(new_board)

            if node_tuple not in seen:
                new_node = Node(new_board, prev=node)
                queue.append((new_node, depth + cost))
                seen.add(node_tuple)

right_corner_zero = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

# Examples from project slides 
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]] 
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]] 
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]] 
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]] 


print(ucs(oh_boy))
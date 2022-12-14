from collections import deque
from helpers import *
from node import Node
import heapq
import time

def misplaced_heuristic(board):
    total_misplaced = 0
    curr = 1

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and board[i][j] != curr:
                total_misplaced += 1
            curr += 1
    return total_misplaced

def manhattan_heuristic(board):
    total_dist = 0
    curr = 1

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and board[i][j] != curr:
                correct_x, correct_y = (board[i][j] - 1) // 3, (board[i][j] - 1) % 3 
                curr_dist = abs(correct_x - i) + abs(correct_y  - j)
                total_dist += curr_dist
    
            curr += 1
    return total_dist

def zero_heuristic(board): 
    return 0

def in_queue(new_board, queue):
    for i in range(len(queue)):
        _, _, node = queue[i]
        if node.board == new_board:
            return i
    return None

def a_star(board, heuristic, timing=False):
    nodes_expanded = 0
    queue = []
    start_fx = heuristic(board)
    start_node = Node(board, start_fx, 0)
    seen = {board_to_tuple(board)}
    heapq.heappush(queue, (start_fx, 0, start_node))
    max_size = 1

    while True:
        if not queue:
            return None
        max_size = max(max_size, len(queue))

        # Get node with min f(x) = g(x) + h(x)
        f_x, g_x, node = heapq.heappop(queue)
        if is_goal_state(node.board):
            if not timing:
                node.printPath()
                print('Goal state!')
                print(f'Solution depth: {g_x}')
                print(f'Nodes expanded: {nodes_expanded}')
                print(f'Max queue size: {max_size}')
            return (node.board, g_x)
        
        # Mark node as visited
        nodes_expanded += 1

        # Generate children and calculate heuristic for each node
        for new_board in get_all_moves(node.board):
            new_board_tuple = board_to_tuple(new_board)
            cost = heuristic(new_board)
            new_fx = g_x + cost + 1
            
            # Add new nodes into queue
            if new_board_tuple not in seen:
                new_node = Node(new_board, new_fx, g_x + 1, prev=node)
                queue.append((new_fx, g_x + 1, new_node))
                seen.add(new_board_tuple)

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

# for heuristic in [zero_heuristic, misplaced_heuristic, manhattan_heuristic]:
    # start = time.time()
    # a_star(depth_24_test, heuristic)
    # end = time.time()

#     print(f'ELAPSED TIME: {end-start}')

from helpers import *

class Node:
    def __init__(self, board, fx, gx, prev=None):
        self.board = board
        self.prev = prev
        self.fx = fx
        self.gx = gx
        self.hx = (fx - gx)
    
    def printPath(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(curr)
            curr = curr.prev
        for curr in reversed(nodes):
            print(f'The best state to expand with a g(n)={curr.gx} and h(n)={curr.hx} is:')
            print_puzzle(curr.board)
    
    def __lt__(self, other):
        return self
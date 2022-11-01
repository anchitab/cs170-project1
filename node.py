from helpers import *

class Node:
    def __init__(self, board, prev=None):
        self.board = board
        self.prev = prev

    def printPath(self):
        curr = self
        while curr:
            print_puzzle(curr.board)
            curr = curr.prev

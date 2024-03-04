from os import *
from sys import *
from collections import *
from math import *

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraph(node):
    oldToNew={}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy=graphNode(node.data)
        oldToNew[node]=copy
        for nei in node.neighbours:
            copy.neighbours.append(dfs(nei))
        return copy

    return dfs(node) if node else None
    pass

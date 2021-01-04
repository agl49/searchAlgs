from math import sqrt

class hfunction():
    def __init__(self, which_h):
        self.h = which_h

    def execute(self, node, dest):
        ans = self.h(node, dest)
        return ans

# h(n) = 0 results in dijkstra's 
def no_H():
    return 0

# Manhattan distance
def manhattan(node, dest):
    dx = abs(node.x - dest.x)
    dy = abs(node.y - dest.y)
    return dx + dy

# Euclidean distance
def euclidean(node, dest):
    dx = (node.x - dest.x) * 2
    dy = (node.y - dest.y) * 2
    return sqrt(dx + dy)

# Diagonal distance
def diagonal(node, dest):
    # Chebyshev distance
    dx = abs(node.x - dest.x)
    dy = abs(node.y - dest.y)
    return 1 * (dx + dy) + (1 - 2) * min(dx, dy)

# Longest Manhattan Distance
def longest_manhattan(node, dest):
    dx = (node.x - dest.x) 
    dy = (node.y - dest.y)
    return max(dx, dy)


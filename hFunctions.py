from math import sqrt
import const

# Weak implementation, could be better
def h_factory(name):
    if name == const.NO_H:
        return no_H

    elif name == const.MAN_DIS:
        return manhattan

    elif name == const.EUCLID:
        return euclidean

    elif name == const.DIAGONAL:
        return diagonal

    elif name == const.LONG_MAN_DIS:
        return longest_manhattan

    else:
        print("Error: incorrect h_name")
        return None

# h(n) = 0 results in dijkstra's 
def no_H(n, dest):
    return 0

# Manhattan distance
def manhattan(n, dest):
    dx = abs(n.x - dest.x)
    dy = abs(n.y - dest.y)
    return dx + dy

# Euclidean distance
def euclidean(n, dest):
    dx = abs(n.x - dest.x)
    dy = abs(n.y - dest.y)
    return 1 * sqrt(dx * dx + dy * dy)

# Diagonal distance
def diagonal(n, dest):
    # Chebyshev distance
    dx = abs(n.x - dest.x)
    dy = abs(n.y - dest.y)
    return 1 * (dx + dy) + (1 - 2) * min(dx, dy)

# Longest Manhattan Distance
# really bad h. Keep?
def longest_manhattan(n, dest):
    dx = (n.x - dest.x)
    dy = (n.y - dest.y)
    return max(dx, dy)


# Strategy pattern with search algs
import pygame
import hFunctions
from display import node
import const
from queue import PriorityQueue

# Each alg needs to return a True or False

# TODO: add algs not done here
def alg_factory(name):
    if name == const.ASTAR:
        return aStar

    elif name == const.DIJKSTRA:
        return dijkstra

    elif name == const.BFS:
        pass

    elif name == const.DFS:
        pass

    else:
        print("Error with alg selection")

# I don't understand why we need current?
# need to know more about loops in python
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_self_path()
        draw()


# A Star search algorithm
# time 1:25:53 and +5 
def aStar(*args):
    h = args[0]
    draw = args[1]
    grid = args[2]
    start = args[3]
    end = args[4]
    rows = args[5]
    cols = args[6]

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    # Better way to do below?
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        # Do we really need this?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = (temp_g_score + 
                                     h(neighbor.get_pos(), end.get_pos()))
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        # This may cause problems
        # This function needs to be draw_grid_window from window class
        draw()

        if current != start:
            current.make_closed()

    return False

# dijkstra
def dijkstra(*args):
    draw = args[0]
    grid = args[1]
    start = args[2]
    end = args[3]
    rows = args[4]
    cols = args[5]

    pass

# Breath first search

# Depth first search


class searchAlg():
    def __init__(self, alg, uses_h = False, h = None):
        try:
            self._h = hFunctions.h_factory(h)
            self._alg = alg_factory(alg)

        except Exception as e:
            print(e)

        self._uses_h = uses_h

    def execute(self, draw, grid, start, end, rows, cols):
        if self._uses_h:
            args = [self._h, draw, grid, start, end, rows, cols]
            return self._alg(*args)
        else:
            args = [draw, grid, start, end, rows, cols]
            return self._alg(*args)



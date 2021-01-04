# Strategy pattern with search algs
import pygame
import hFunctions
import display

class alg():
    def __init__(self, alg, uses_h = False, h = None):
        self._alg = alg
        self._uses_h = uses_h
        self._h = h

    def execute(self, draw, grid, start, end):
        if self._uses_h:
            return self._alg(self._h, draw, grid, start, end)
        else:
            return self._alg(draw, grid, start, end)


# A Star search algorithm
# time 1:25:53 and +5 

# dijkstra

# Breath first search

# Depth first search

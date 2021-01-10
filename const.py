# These are just constants that will
# use in a bunch of files
from enum import Enum

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class buttonMode(Enum):
     BOOL = 1
     CALLBACK = 2

ASTAR = "1"
DFS = "2"
# BFS = "3"
# DFS = "4"

ALG_SET = {ASTAR, DFS}

NO_H = "1"
MAN_DIS = "2"
EUCLID = "3"
DIAGONAL = "4"
LONG_MAN_DIS = "5"

H_SET = {NO_H, MAN_DIS, EUCLID, DIAGONAL, 
         LONG_MAN_DIS}

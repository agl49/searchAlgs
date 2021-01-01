# Has functions for input and interaction with the user
import pygame

# TODO: problem with the x y and indexing through the grid[][]
def get_clicked_position(pos, cols, width):
    gap = width // cols
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col


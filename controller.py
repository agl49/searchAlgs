# Has functions for input and interaction with the user
import pygame

def get_clicked_position(pos, cols, width):
    gap = width // cols
    x, y = pos

    row = y // gap
    col = x // gap

    # debugging
    # print(f"pos: {pos}")
    # print(f"col and row: {col, row}")

    return row, col


# This will handle the window for the demo.
# As a result, this will hold the functions for the pygame game loops
import pygame
import const
from collections import namedtuple

#Defines each node in the demonstration
class node:
    def __init__(self, row, col, width, total_rows, total_col):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = const.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_col

    #returns row col position
    def get_pos(self):
        my_position = namedtuple("my_position", ["x", "y"])
        p = my_position(self.col, self.row)
        return p

    #Determines if node a node has been visited
    def is_visited(self):
        return self.color == const.RED

    #Determines if the node is open for exploration
    def is_open(self):
        return self.color == const.GREEN

    def is_barrier(self):
        return self.color == const.BLACK

    def is_start(self):
        return self.color == const.ORANGE

    def is_end(self):
        return self.color == const.TURQUOISE

    def reset(self):
        self.color = const.WHITE

    def make_start(self):
        self.color = const.ORANGE

    def make_closed(self):
        self.color = const.RED

    def make_open(self):
        self.color = const.GREEN

    def make_barrier(self):
        self.color = const.BLACK

    def make_end(self):
        self.color = const.TURQUOISE

    def make_self_path(self):
        self.color = const.PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        
        try:
            # Down
            if (self.row < self.total_rows - 1 and not 
                        grid[self.row + 1][self.col].is_barrier()):
                self.neighbors.append(grid[self.row + 1][self.col])

            # Up
            if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
                self.neighbors.append(grid[self.row - 1][self.col])

            # Right
            if (self.col < self.total_cols - 1 and 
                    not grid[self.row][self.col + 1].is_barrier()):
                self.neighbors.append(grid[self.row][self.col + 1])

            # Left
            if (self.col > 0 and not grid[self.row][self.col - 1].is_barrier()):
                self.neighbors.append(grid[self.row][self.col - 1])

        except Exception as e:
            print(e)
            print(f"self.row and col: {self.row} {self.col}")
            raise

        
    #Defines less than < operation for object
    def __lt__(self, other):
        return False


class window:
    def __init__(self, width = 900):
        self._width = width
        self.window = pygame.display.set_mode((self._width, self._width))
        # Caption for the window
        pygame.display.set_caption("Search Alg demo")

    #Default values to prevent error with range()
    #Makes grid 2d array that used to present data 
    def make_grid(self, rows = 1, cols = 1, width = 1):
        grid = []
        gap = width // cols
        demo_height = rows * gap
        demo_width = cols * gap
        
        # For now, grid is created from 0,0 for its starting point
        grid_container = pygame.Rect(0, 0, demo_width, demo_height)
        # Fill the grid with nodes
        # debugging
        # print(f"rows input:{rows}")

        for y in range(rows):
            grid.append([])
            for x in range(cols):
                # debugging
                # print(f"node is : {type(node)}")

                new_node = node(y, x, gap, rows, cols)
                grid[y].append(new_node)

        return grid, grid_container

    def draw_grid(self, rows, cols, width):
        gap = width // cols
        demo_height = rows * gap

        for i in range(rows):
            #Draw the horizontal lines
            pygame.draw.line(self.window, const.GREY, (0, i * gap), 
                             (width, i * gap))
            for j in range(cols):
                #Draw the vertical lines
                pygame.draw.line(self.window, const.GREY, (j * gap, 0), 
                                 (j * gap, demo_height))

    def draw_grid_window(self, grid, rows, cols, grid_width, grid_container):
        #Fills window with white
        self.window.fill(const.WHITE)

        #Draw each node object in the grid
        for row in grid:
            # Debugging
            # print(f"row length:{len(row)}")
            for n in row:
                n.draw(self.window)

        self.draw_grid(rows, cols, grid_width)
        pygame.draw.rect(self.window, const.BLACK, grid_container, 5)

        # May have to remove this update
        # pygame.display.update()

    def alg_draw_grid(self, grid, rows, cols, grid_width, grid_container):
        #Fills window with white
        self.window.fill(const.WHITE)

        #Draw each node object in the grid
        for row in grid:
            # Debugging
            # print(f"row length:{len(row)}")
            for n in row:
                n.draw(self.window)

        self.draw_grid(rows, cols, grid_width)
        pygame.draw.rect(self.window, const.BLACK, grid_container, 5)

        # May have to remove this update
        pygame.display.update()

    def draw_normal_window(self):
        self.window.fill(const.WHITE)



# This will handle the window for the demo.
# As a result, this will hold the functions for the pygame game loops
import pygame
import const

#Defines each node in the demonstration
class node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = const.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    #returns row col position
    def get_pos(self):
        return self.row, self.col

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
        pass

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
    def make_grid(self, rows = 1, width = 1):
        grid = []
        gap = width // rows
        #Fill the grid with nodes
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                new_node = node(i, j, gap, rows)
                grid[i].append(new_node)

        return grid

    def draw_grid(self, rows, width):
        gap = width // rows
        for i in range(rows):
            #Draw the horizontal lines
            pygame.draw.line(self.window, const.GREY, (0, i * gap), 
                             (width, i * gap))
            for j in range(rows):
                #Draw the vertical lines
                pygame.draw.line(self.window, const.GREY, (j * gap, 0), 
                                 (j * gap, width))

    def draw_grid_window(self, grid, rows):
        #Fills window with white
        self.window.fill(const.WHITE)

        #Draw each node object in the grid
        for row in grid: 
            for n in grid:
                n.draw(self.window)

        self.draw_grid(rows, self._width)
        pygame.display.update()

    def draw_normal_window(self):
        self.window.fill(const.WHITE)


# Display options menu function
# def displayMenu():
    

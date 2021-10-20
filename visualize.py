import pygame as pg
import sys
import life
from pygame.locals import *
from typing import Optional, List, Tuple


class MatrixVizualizer:

    def __init__(self,
        base_matrix: List,
        mode: int,
        delay: float,
        bg_color: Tuple,
        cell_color: Tuple,
        width = 400,
        height = 400) -> None:
        """
        Explanation of arguments:
        - base_matrix : matrix which we start our game with
        - mode : int value of mode we gonna simulate game in
         (1 - non-interactive, 2 - interactive, 3 - interactive with grid)

        - delay : period of time between two screen refreshes
        - bg_color: color of grid or background of screen
        - cell_color: color of cells
        - width, height : dimensions of screen

        """

        self.width = width
        self.height = height

        self.bg_color = bg_color
        self.cell_color = cell_color

        self.mode = mode

        # initializing pygame window
        self.fps = 30
        self.CLOCK = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Vizualize matrixes")
        self.screen = pg.display.set_mode((self.width, self.height), RESIZABLE)

        self.matrix = base_matrix

        self.mrow = len(self.matrix)    # count of rows in matrix
        self.mcolumn = len(self.matrix[0])  # count of columns in matrix

        self.starting_margin = self.width // self.mrow // 10 # left margin
        self.ending_margin = self.width // self.mrow // 5   # right margin

        self.grid_node_width = self.width // self.mcolumn
        self.grid_node_height = self.height // self.mrow

        self.MOVEEVENT, t = pg.USEREVENT+1, delay
        pg.time.set_timer(self.MOVEEVENT, t)

        if self.mode == 3:  # We want grid only in particular mode
            self.initialize_grid()

    def initialize_grid(self) -> None:

        line_color = self.cell_color
        self.screen.fill(self.bg_color)

        counter = 1 # how many lines we alredy did
        for l in range(self.mcolumn):

            # Drawing vertical lines
            pg.draw.line(self.screen, line_color, (self.width//self.mcolumn *
                                                   counter, 0), (self.width//self.mcolumn * counter, self.height), 7)
            counter += 1

        counter = 1
        for l in range(self.mrow):

            # Drawing horizontal lines
            pg.draw.line(self.screen, line_color,
                         (0, self.height//self.mrow * counter), (self.width, self.height//self.mrow * counter), 7)
            counter += 1

        pg.display.update()


    def createSquare(self, x: int, y: int, color: Tuple) -> None:
        pg.draw.rect(self.screen, color, [
                     x + self.starting_margin, y + self.starting_margin,
                      self.grid_node_width - self.ending_margin, self.grid_node_height - self.ending_margin])


    def draw_matrix(self, data: List[List[int]]) -> None:

        y = 0  # we start at the top of the screen
        for row in data:
            x = 0  # for every row we start at the left of the screen again
            for item in row:
                if item == 0:
                    self.createSquare(x, y, self.bg_color)
                else:
                    self.createSquare(x, y, self.cell_color)

                # for ever item/number in that row we move one "step" to the right
                x += self.grid_node_width
            y += self.grid_node_height   # for every new row we move one "step" downwards

        pg.display.update()


    def click(self) -> None:
        """
        Event method for click
        """
        self.matrix = life.life(self.matrix, 1)
        self.draw_matrix(self.matrix)


    def resize(self, w: int, h: int) -> None:
        """
        Draws resized window
        """

        self.width = w
        self.height = h
        self.screen = pg.display.set_mode((self.width, self.height), RESIZABLE)

        pg.display.update()


    def run_winteract(self) -> None:
        """
        Pygame loop : non-interactive mode
        """
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    # Window quit
                    pg.quit()
                    sys.exit()

                elif event.type == self.MOVEEVENT:
                    self.click()

            pg.display.update()
            self.CLOCK.tick(self.fps)


    def run_interact(self) -> None:
        """
        Pygame loop : interactive mode
        """
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    # Window quit
                    pg.quit()
                    sys.exit()

                elif event.type is MOUSEBUTTONDOWN:
                    # Click
                    self.click()

            pg.display.update()
            self.CLOCK.tick(self.fps)

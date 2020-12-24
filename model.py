# Here should be the game loops used for the game
# maybe...
import controller
from display import window
import pygameGUI
import const
import pygame
import sys

# test game loop
# for testing and debugging GUI elements

def testGUI(mainClock):
    # TODO this needs fixing, the order in which
    # things happen
    # simple text input dictionary
    kwargs = {"x": 50, 
              "y": 80,
              "width": 100,
              "height": 100,
              "pos": pygame.math.Vector2(50, 80), 
              "size": pygame.math.Vector2(100, 100),
              "bg_color": const.GREY,
              "active_color": const.GREEN,
              "text_size": 25,
              "text_color": const.WHITE,
              "boarder_color": const.BLACK,
              "boarder": 5}

    testTextBox1 = pygameGUI.simpleTextInput(**kwargs)

    textBoxes = []
    textBoxes.append(testTextBox1)

    testTextLable = pygameGUI.simpleTextLable("test label")

    menuWindow = window()
    menuWindow.draw_normal_window()

    testButton = pygameGUI.Button(500, 500, "test me")

    running = True
    while running:

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in textBoxes:
                    box.check_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                for box in textBoxes:
                    if box.active:
                        box.add_text()

        mainClock.tick(60)


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

def testFunctForButton(a, b):
    print(f"callback function {a} + {b}: {a + b}")
    return a + b

def diffTestFunction(a, b, c):
    ans = a + b + c
    print(f"Different callback function {a} + {b} + {c}: {ans}")
    return ans

def testGUI(mainClock):
    # TODO this needs fixing, the order in which
    # things happen
    # simple text input dictionary
    kwargs = {"x": 400, 
              "y": 200,
              "width": 200,
              "height": 50,
              "pos": pygame.math.Vector2(400, 200), 
              "size": pygame.math.Vector2(200, 50),
              "bg_color": const.GREY,
              "active_color": const.RED,
              "text_size": 25,
              "text_color": const.WHITE,
              "boarder_color": const.BLACK,
              "boarder": 5}

    kwargs2 = {"x": 400, 
              "y": 400,
              "width": 200,
              "height": 50,
              "pos": pygame.math.Vector2(400, 400), 
              "size": pygame.math.Vector2(200, 50),
              "bg_color": const.BLUE,
              "active_color": const.RED,
              "text_size": 25,
              "text_color": const.WHITE,
              "boarder_color": const.BLACK,
              "boarder": 5}

    menuWindow = window()
    menuWindow.draw_normal_window()

    testTextBox1 = pygameGUI.simpleTextInput(**kwargs)
    testTextBox2 = pygameGUI.simpleTextInput(**kwargs2)

    textBoxes = []
    textBoxes.append(testTextBox1)
    textBoxes.append(testTextBox2)

    testTextLable = pygameGUI.simpleTextLable("test label")
    testTextLable.set_font(pygame.font.SysFont("Ubuntu Mono", 30), 25, const.BLUE,
                           True)

    testButton = pygameGUI.Button(400, 100, "test me long string the ", 
                                  const.buttonMode.CALLBACK, 
                                  testFunctForButton, [1, 2])
    
    testButton2 = pygameGUI.Button(400, 300, "button 2 callback", 
                                  const.buttonMode.CALLBACK, 
                                  diffTestFunction, [1, 1, 1])


    buttonCallbackOut1 = None
    buttonCallbackout2 = None
    running = True
    textBoxOutput1 = None
    while running:
        pressed1 = False
        pressed2 = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                for box in textBoxes:
                    box.check_click()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                for box in textBoxes:
                    if box.active:
                        box.add_text(event)

            pressed1, buttonCallbackOut1 = testButton.drawButton(event, menuWindow)
            pressed2, buttonCallbackout2 = testButton2.drawButton(event, menuWindow)

        for box in textBoxes:
            box.draw(menuWindow.window)

        testTextLable.draw(menuWindow.window, (400, 50))

        if pressed1 == True: 
            print("button pressed")
            print(f"callback output: {buttonCallbackOut1}")
            print("Changing text of label")
            testTextLable.change_text("new text")

        if pressed2 == True:
            print("second button pressed")
            print(f"callback output: {buttonCallbackout2}")
            print("Changing font of label")
            testTextLable.change_text("different text")

        for box in textBoxes:
            if not box.active and box.modified:
                textBoxOutput1 = box.return_text()
                print(f"Text box input = {textBoxOutput1}")

        pygame.display.update()
        mainClock.tick(60)


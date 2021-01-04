# Here should be the game loops used for the game
# maybe...
from controller import get_clicked_position
from display import window
from display import node
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

            testButton.get_event(event)
            testButton2.get_event(event)

        pressed1, buttonCallbackOut1 = testButton.drawButton(menuWindow)
        pressed2, buttonCallbackout2 = testButton2.drawButton(menuWindow)

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


def main_menu_test(mainClock):
    menuWindow = window()
    menuWindow.draw_normal_window()

    testTextLable = pygameGUI.simpleTextLable("Main menu")
    testTextLable.set_font(pygame.font.SysFont("Ubuntu Mono", 30), 25, 
                           const.BLACK, True)

    toGameButton = pygameGUI.Button(400, 700, "to game", 
                                  const.buttonMode.BOOL)

    running = True
    
    while running:
        toGame = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            toGameButton.get_event(event)

        toGame = toGameButton.drawButton(menuWindow)[0]

        testTextLable.draw(menuWindow.window, (400, 50))

        if toGame:
            print("Changing to demo")
            menuWindow.draw_normal_window()
            demo_test(mainClock)
            print("finished demo")

        pygame.display.update()
        mainClock.tick(60)

def demo_test(mainClock):
    menuWindow = window()
    menuWindow.draw_normal_window()

    testTextLable = pygameGUI.simpleTextLable("Demo")
    testTextLable.set_font(pygame.font.SysFont("Ubuntu Mono", 30), 25, 
                           const.BLACK, True)

    toMenuButton = pygameGUI.Button(400, 600, "to menu", 
                                  const.buttonMode.BOOL)

    running = True
    
    while running:
        toMenu = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
            toMenuButton.get_event(event)

        toMenu = toMenuButton.drawButton(menuWindow)[0]

        testTextLable.draw(menuWindow.window, (400, 150))

        if toMenu:
            print("Changing to menu")
            menuWindow.draw_normal_window()
            running = False

        pygame.display.update()
        mainClock.tick(60)

def menu(mainClock):
    menu_window = window()
    menu_window.draw_normal_window()

    title = pygameGUI.simpleTextLable("Search algorithm demo")
    title.set_font(pygame.font.SysFont("Times New Roman", 30), 1, const.BLACK, 
                   True)
    # Other menu UI elements here

    toDemoButton = pygameGUI.Button(300, 800, "Start Demo", 
                                    const.buttonMode.BOOL)

    running = True

    # Menu Loop
    while running:
        toDemo = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
            # Buttons get events section
            toDemoButton.get_event(event)

        # buttons section
        toDemo = toDemoButton.drawButton(menu_window)[0]

        # Text section
        title.draw(menu_window.window, (400, 50))

        # Window change
        if toDemo:
            menu_window.draw_normal_window()
            demo(mainClock, 50, 900)

        pygame.display.update()
        mainClock.tick(60)

def demo(mainClock, rows, window_width):
    demo_window = window(window_width)

    # Space of the window that the demo will take place
    # demo_space = window_width - 100

    start_node = None
    end_node = None

    rows = 40
    cols = 45
    grid, grid_container = demo_window.make_grid(rows, cols, window_width)    

    running = True
    alg_start = False

    # Updates these positions
    toMenuButton = pygameGUI.Button(200, 820, "Return to Menu", 
                                    const.buttonMode.BOOL)
    restartButton = pygameGUI.Button(750, 820, "Reset", const.buttonMode.BOOL)

    # Text items to add to the window, such as instructions on how to use the 
    # demo

    running = True

    # Algorithm demo loop
    while running:
        toMenu = False
        restart = False

        demo_window.draw_grid_window(grid, rows, cols, window_width, grid_container)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if alg_start:
                continue

            if pygame.mouse.get_pressed()[0]: # Left mouse button
                pos = pygame.mouse.get_pos()

                if grid_container.collidepoint(pos):
                    row, col = get_clicked_position(pos, cols, window_width)
                    # Debugging
                    # print(f"row: {row}, col: {col}")

                    spot = grid[row][col]
                    if not start_node and spot != end_node:
                        start_node = spot
                        start_node.make_start()

                    elif not end_node and spot != start_node:
                        end_node = spot
                        end_node.make_end()

                    elif spot != end_node and spot != start_node:
                        spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # Right mouse button
                # This section allows for the erasure of selected nodes 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, cols, window_width)
                spot = grid[row][col]
                spot.reset()
                if spot == start_node:
                    start_node = None
                elif spot == end_node:
                    end_node = None

            # Buttons get events
            toMenuButton.get_event(event)
            restartButton.get_event(event)

        # Buttons section 
        toMenu = toMenuButton.drawButton(demo_window)[0]
        restart = restartButton.drawButton(demo_window)[0]

        if toMenu:
            print("toMenu pressed")
            demo_window.draw_normal_window()
            running = False

        if restart:
            print("restart pressed")


        # Text section


        pygame.display.update()
        mainClock.tick(60)





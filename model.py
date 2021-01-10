# Here should be the game loops used for the game
# maybe...
from controller import get_clicked_position
from display import window
from display import node   # TODO: search for this and make sure we don't need this
import pygameGUI           # so we can remove it
import const
import pygame
import sys
import alg
import hFunctions

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

    # Text elements
    title = pygameGUI.simpleTextLable("Search algorithm demo")
    title.set_font(pygame.font.SysFont("Times New Roman", 30), 1, const.BLACK, 
                   True)
    
    alg_instructions_1 = pygameGUI.simpleTextLable("Please type the number of "
                                                   "the algorithm you wish to " 
                                                   "demo.")

    alg_instructions_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                                const.BLACK, True)

    valid_input_1 = pygameGUI.simpleTextLable("Invalid")
    valid_input_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

    alg_options = pygameGUI.simpleTextLable("1-aStar/dijkstra/Bfs 2-Dfs")
    alg_options.set_font(pygame.font.SysFont("Times New Roman", 28), 1, 
                         const.BLACK, True)

    alg_instructions_2 = pygameGUI.simpleTextLable("1 serves as A* if a h is "
                                                   "selected. Otherwise it's"
                                                   " BFS or Dijkstra's")
    alg_instructions_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                                const.BLACK, True)

    alg_instructions_3 = pygameGUI.simpleTextLable("with a travel cost of 1.")
    alg_instructions_3.set_font(pygame.font.SysFont("Times New Roman", 30), 1,
                               const.BLACK, True)

    valid_input_2 = pygameGUI.simpleTextLable("Invalid")
    valid_input_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

    h_options_1 = pygameGUI.simpleTextLable("1-no_h 2-Manhatten distance "
                                            "3-Euclidean 4-Diagonal Distance")
    h_options_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                         const.BLACK, True)

    h_options_2 = pygameGUI.simpleTextLable("5-Longest Manhatten Distance")
    h_options_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                         const.BLACK, True)

    controls_1 = pygameGUI.simpleTextLable("Right mouse button to place the " 
                                           "start, end and wall nodes.")
    controls_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                         const.BLACK, True)

    controls_2 = pygameGUI.simpleTextLable("Left mouse button to reset a node.")
    controls_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                         const.BLACK, True)

    demo_status = pygameGUI.simpleTextLable("Not Ready")
    demo_status.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

    # Text input elements
    kwargs = {"x": 100, 
              "y": 150,
              "width": 50,
              "height": 50,
              "pos": pygame.math.Vector2(100, 150), 
              "size": pygame.math.Vector2(50, 50),
              "bg_color": const.GREY,
              "active_color": const.RED,
              "text_size": 15,
              "text_color": const.WHITE,
              "boarder_color": const.BLACK,
              "boarder": 5}

    kwargs2 = {"x": 100, 
              "y": 400,
              "width": 50,
              "height": 50,
              "pos": pygame.math.Vector2(100, 400), 
              "size": pygame.math.Vector2(50, 50),
              "bg_color": const.GREY,
              "active_color": const.RED,
              "text_size": 15,
              "text_color": const.WHITE,
              "boarder_color": const.BLACK,
              "boarder": 5}


    text_box_1 = pygameGUI.simpleTextInput(**kwargs)
    text_box_2 = pygameGUI.simpleTextInput(**kwargs2)

    text_boxes = []
    text_boxes.append(text_box_1)
    text_boxes.append(text_box_2)

    # Button elements
    toDemoButton = pygameGUI.Button(300, 800, "Start Demo", 
                                    const.buttonMode.BOOL)

    running = True
    text_input_1 = None
    text_input_2 = None
    alg_choice_good = False
    h_choice_good = False
    demo_ready = False
    # Menu Loop
    while running:
        toDemo = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                for box in text_boxes:
                    box.check_click()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                for box in text_boxes:
                    if box.active:
                        box.add_text(event)
        
            # Buttons get events section
            toDemoButton.get_event(event)

        # buttons section
        toDemo = toDemoButton.drawButton(menu_window)[0]

        # Text input section
        for box in text_boxes:
            box.draw(menu_window.window)

        # Text section
        title.draw(menu_window.window, (300, 30))
        alg_instructions_1.draw(menu_window.window, (100, 100))
        valid_input_1.draw(menu_window.window, (170, 155))
        alg_options.draw(menu_window.window, (100, 230))
        alg_instructions_2.draw(menu_window.window, (100, 300))
        alg_instructions_3.draw(menu_window.window, (100, 350))
        valid_input_2.draw(menu_window.window, (170, 405))
        h_options_1.draw(menu_window.window, (100, 480))
        h_options_2.draw(menu_window.window, (100, 510))
        controls_1.draw(menu_window.window, (100, 600))
        controls_2.draw(menu_window.window, (100, 650))
        demo_status.draw(menu_window.window, (500, 800))

        # Text output
        for box in text_boxes:
            if not box.active and box.modified:
                if box is text_box_1:
                    text_input_1 = box.return_text()
                elif box is text_box_2:
                    text_input_2 = box.return_text()

        # Validate settings
        if text_input_1 in const.ALG_SET:
            alg_choice_good = True
        else:
            alg_choice_good = False
        
        if text_input_2 in const.H_SET and text_input_1 == const.ASTAR:
            h_choice_good = True
        elif text_input_1 != const.ASTAR and text_input_2 == const.NO_H:
            h_choice_good = True
        else:
            h_choice_good = False

        demo_ready = alg_choice_good and h_choice_good

        # Update Validation feedback
        if alg_choice_good:
            valid_input_1.change_text("Valid")
            valid_input_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.BLUE, True)
        else:
            valid_input_1.change_text("Invalid")
            valid_input_1.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

        if h_choice_good:
            valid_input_2.change_text("Valid")
            valid_input_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.BLUE, True)
        else:
            valid_input_2.change_text("Invalid")
            valid_input_2.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

        if demo_ready:
            demo_status.change_text("Valid")
            demo_status.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.BLUE, True)
        else:
            demo_status.change_text("Invalid")
            demo_status.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)


        # Window change
        if toDemo and demo_ready:
            menu_window.draw_normal_window()
            demo(mainClock, 50, 900, text_input_1, text_input_2)

        pygame.display.update()
        mainClock.tick(60)

def demo(mainClock, rows, window_width, alg_choice, h_choice):
    demo_window = window(window_width)

    # Algorithm Strategy
    if alg_choice == const.ASTAR:
        # A Star
        strategy = alg.searchAlg(alg_choice, True, h_choice)

    else:
        # Non-A Star
        strategy = alg.searchAlg(alg_choice, False, h_choice)

    start_node = None
    end_node = None

    rows = 40
    cols = 45
    grid, grid_container = demo_window.make_grid(rows, cols, window_width)    

    running = True
    path_found = False 

    # Buttons
    toMenuButton = pygameGUI.Button(50, 820, "Return to Menu", 
                                    const.buttonMode.BOOL)
    restartButton = pygameGUI.Button(700, 820, "Reset", const.buttonMode.BOOL)

    start_button = pygameGUI.Button(500, 820, "Start", const.buttonMode.BOOL)

    # Text
    found = pygameGUI.simpleTextLable("No Path")
    found.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

    running = True

    # Algorithm demo loop
    while running:
        toMenu = False
        restart = False
        begin_alg = False

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

            if pygame.mouse.get_pressed()[0]: # Left mouse button
                pos = pygame.mouse.get_pos()

                if grid_container.collidepoint(pos):
                    row, col = get_clicked_position(pos, cols, window_width)

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
            start_button.get_event(event)

        # Buttons section 
        toMenu = toMenuButton.drawButton(demo_window)[0]
        restart = restartButton.drawButton(demo_window)[0]
        begin_alg = start_button.drawButton(demo_window)[0]

        # Text section
        found.draw(demo_window.window, (300, 820))


        if toMenu:
            print("toMenu pressed")
            demo_window.draw_normal_window()
            running = False

        if restart:
            print("restart pressed")
            start_node = None
            end_node = None
            grid, grid_container = demo_window.make_grid(rows, cols, 
                                                         window_width)   
            path_found = False


        # 1:27:20
        if begin_alg and start_node != None and end_node != None:
            print("running alg")
            # alg_running = True
            for row in grid:
                for spot in row:
                    spot.update_neighbors(grid)

            # could be re factored to be shorter
            path_found = strategy.execute(lambda: demo_window.alg_draw_grid(
                grid, rows, cols, window_width, grid_container), 
                                          grid, start_node, end_node, rows, cols)

        # update feedback
        if path_found:
            found.change_text("Path Found")
            found.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.BLUE, True)
        else:
            found.change_text("No Path")
            found.set_font(pygame.font.SysFont("Times New Roman", 30), 1, 
                           const.RED, True)

        pygame.display.update()
        mainClock.tick(60)





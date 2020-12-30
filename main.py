import pygame
from pygame.locals import *
import model

mainClock = pygame.time.Clock()
pygame.init()



def main():
    #main function
    #add the other classes here
    
    # Test GUI elements
    # model.testGUI(mainClock)

    # Test Window switching
    model.main_menu_test(mainClock)

    pygame.quit()

if __name__ == "__main__":
    main()


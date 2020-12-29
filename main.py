import pygame
from pygame.locals import *
import model

mainClock = pygame.time.Clock()
pygame.init()



def main():
    #main function
    #add the other classes here
    
    # Test GUI elements
    model.testGUI(mainClock)

    pygame.quit()

if __name__ == "__main__":
    main()


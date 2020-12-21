# This contains classes related to pygame GUI creation
# This is mainly for quick and dirty ui elements.
# Use a separate module for more a more in depth GUI
# Current implementation only takes in callbacks with list
# as args
import pygame
import const


class simpleTextLable:
    def __init__(self, text):
        self._text = text

#bool based button class
class Button:
    #button class variables
    WIDTH = 180
    HEIGHT = 40
    DEFAULT_COL = const.GREY
    DEFAULT_TEXT_COL = const.BLACK

    def __init__(self, x, y, text, screen, type = const.buttonMode.BOOL, 
                 callback = None, args = None):
        self.x = x
        self.y = y
        self.text = text
        self.button_col = Button.DEFAULT_COL
        self.hover_col = Button.DEFAULT_COL
        self.click_col = Button.DEFAULT_COL
        self.text_col = Button.DEFAULT_TEXT_COL
        self.screen = screen
        self._font = pygame.font.SysFont("Constantia", 30)
        if type == const.buttonMode.CALLBACK:
            assert callable(callback), ("callback must be a function in " 
                                        "callback mode")
        self.type = type
        self.callback = callback
        self.args = args

        # TODO do the tags in this project
        # also implement this in such a way that it can either
        # return a bool or a callback when pressed

    def changeFont(self, new_font):
        self._font = new_font


    def changeColors(self, button_col, hover_col, click_col, text_col):
        self.button_col = button_col
        self.hover_col = hover_col
        self.click_col = click_col
        self.text_col = text_col

    def __executeCallBack(self):
        return self.callback(*self.args)

    def drawButton(self, events):
        update = False

        #Rectangle object of button
        button_rect = pygame.Rect(self.x, self.y, Button.WIDTH, Button.HEIGHT)
        
        for event in events:  # type should be pygame.event.Event
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(*event.pos):
                    pygame.draw.rect(self.screen, self.click_col, button_rect)

            elif event.type == pygame.MOUSEBUTTONUP:
                if button_rect.collidepoint(*event.pos):
                    # TODO check to see if below is needed, but I feel like it is
                    pygame.draw.rect(self.screen, self.button_col, button_rect)
                    # execute callback function if set
                    if self.type == const.buttonMode.CALLBACK:
                        self.__executeCallBack()
                    update = True

            else:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.screen, self.hover_col, button_rect)
                else:
                    pygame.draw.rect(self.screen, self.button_col, button_rect)

        # add shading to the buttons
        pygame.draw.line(self.screen, const.WHITE, (self.x, self.y), 
                        (self.x + Button.WIDTH, self.y), 2)
        pygame.draw.line(self.screen, const.WHITE, (self.x, self.y), 
                        (self.x, self.y + Button.HEIGHT), 2)
        pygame.draw.line(self.screen, const.BLACK, 
                        (self.x, self.y + Button.HEIGHT), 
                        (self.x + Button.WIDTH, self.y + Button.HEIGHT), 2)
        pygame.draw.line(self.screen, const.BLACK, 
                        (self.x + Button.WIDTH, self.y),
                        (self.x + Button.WIDTH, self.y + Button.HEIGHT), 2) 
        
        # add text to the button
        text_img = self._font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.screen.blit(text_img, 
                         self.x + int(Button.WIDTH / 2) - int(text_len / 2), 
                         self.y + 5)
        return update

# This contains classes related to pygame GUI creation
# This is mainly for quick and dirty ui elements.
# Use a separate module for more a more in depth GUI
# Current implementation only takes in callbacks with list
# as args
import pygame
import const

# Not sure why just calling it in the main file is not enough
pygame.init()

# TODO The boarder var currently only serves as a buffer for the text and the 
# edge of the box, and does not acutally render into a boarder. Not sure if 
# we want to change that in the future
class simpleTextInput:

    # Dictionary inputs
    # "x" = int pixel position on screen
    # "y" = int pixel position on screen
    # "width" = int pixel width
    # "height" = int pixel width
    # "pos" = pygame.math.Vector2(x,y) Same x and y as above 
    # "size" = pygame.math.Vector2(width, hight)
    # "bg_color" = (#, #, #) of a color code
    # "active_color" = (#, #, #) of a color code
    # "text_size" = int 
    # "text_color" = (#, #, #) of a color code
    # "boarder_color" = (#, #, #) of a color code
    # "boarder" = int thickness of boarder 
    def __init__(self, **kwargs):
        self._x = kwargs["x"]
        self._y = kwargs["y"]
        self._width = kwargs["width"]
        self._height = kwargs["height"]
        self._pos = kwargs["pos"]
        self._size = kwargs["size"]  # TODO problems with surface location  
        self._image = pygame.Surface((self._width, self._height))
        self._rect =  pygame.Rect(self._x, self._y, self._width, self._height)
        self._bg_color = kwargs["bg_color"]
        self.active_color = kwargs["active_color"]
        self.active = False
        self.text = ""
        self.text_size = 24 or kwargs["text_size"]
        self._font = pygame.font.SysFont("Times New Roman", self.text_size)
        self._text_color = kwargs["text_color"]
        self._boarder_color = kwargs["boarder_color"]
        self._boarder = kwargs["boarder"]

        self.modified = False
    
    def check_click(self):
        self.active = self._rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        # check time 39:47
        if (self._boarder == 0) and not self.active:
            self._image.fill(self._bg_color)

        elif (self._boarder == 0) and self.active:
            self._image.fill(self.active_color)

        else:
            if self.active:
                self._image.fill(self.active_color)
            else:
                self._image.fill(self._bg_color)

            pygame.draw.rect(self._image, self._boarder_color, self._rect, 
                             self._boarder)
        
        text = self._font.render(self.text, False, self._text_color)
        text_height = text.get_height()
        text_width = text.get_width()
        # For allowing texts strings longer than the box
        if text_width < (self._width - self._boarder * 2):
            self._image.blit(text, (self._boarder * 2, 
                                   (self._height - text_height)//2))
        else: 
            self._image.blit(text, 
                            ((self._boarder * 2) + 
                             (self._width - text_width - self._boarder * 3), 
                            (self._height - text_height)//2))

        
        surface.blit(self._image, self._pos)

    def add_text(self, event):
        self.modified = True

        try:
            key = event.key
            unicode = event.unicode

            # Backspace
            if key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
                if self.text:
                    text = list(self.text)
                    text.pop()
                    self.text = "".join(text)

            # Space Bar
            elif key == pygame.K_SPACE:
                text = list(self.text)
                text.append(" ")
                self.text = "".join(text)

            # tab
            elif key == pygame.K_TAB:
                text = list(self.text)
                text.append("   ")
                self.text = "".join(text)

            elif (31 < key < 127 or 255 < key < 266):
                self.text += unicode

            elif key == pygame.K_RETURN:
                self.active = False

            else:
                # Key not accepted
                print(f"Key not accepted: {key}")

        except Exception as ex:
            print(f"Problem key: {event.key}")
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    def return_text(self):
        if not self.active:
            self.modified = False
            return self.text

# TODO Right now, this only works with a white background. You need to 
# maybe modify it so that it will work with any color background. 
# Otherwise it'll work for our project.
# TODO Right now, the self._font_size is not used
class simpleTextLable:
    def __init__(self, text):
        self._text = text
        self._previousWeight = 0   # Default values since surface won't
        self._previousHeight = 0   # accept None values
        self._white_surface = None

    def set_font(self, font = pygame.font.SysFont("Times New Roman", 30), 
                 font_size = 12, color = const.BLACK, antialias = True):
        self._font = font
        self._font_size = font_size
        self._color = color
        self._antialias = antialias

    def change_text(self, text):
        self._text = text

    # This is mainly to make give flexibility to text instantiation
    def _render_font(self, text, color = (0, 0, 0)):
        assert isinstance(color, tuple), "Color is not tuple"

        return self._font.render(text, self._antialias, color)

    def _render_string(self):
        text = self._render_font(self._text, self._color)

        # For erasing previous text
        if self._previousHeight == 0 and self._previousWeight == 0:
            self._previousWeight = int(text.get_width())
            self._previousHeight = int(text.get_height())
            
        else:
            self._white_surface = pygame.Surface((int(self._previousWeight),
                                            int(self._previousHeight)))
            self._white_surface.fill(const.WHITE)
            self._previousHeight = 0
            self._previousWeight = 0



        text_surface = pygame.Surface((int(text.get_width()), 
                                       int(text.get_height())), 
                                      pygame.SRCALPHA, 32)

        # Making surface optimized for alpha based transparency 
        text_surface = pygame.Surface.convert_alpha(text_surface)

        text_surface.blit(text, (0,0))
        
        # new_width = text_surface.get_size()[0]
        new_hight = text_surface.get_size()[1]

        text_surface = pygame.transform.smoothscale(text_surface, 
                                                    (text.get_width(), 
                                                     new_hight))

        return text_surface

    def draw(self, surface, pos):
        self._surface = self._render_string()
        
        if self._white_surface is not None:
            surface.blit(self._white_surface, pos)

        surface.blit(self._surface, pos) 

class Button:
    #button class variables
    WIDTH = 180
    HEIGHT = 40
    DEFAULT_COL = const.GREY
    DEFAULT_HOVER_COL = const.BLUE
    DEFAULT_CLICK_COL = const.RED
    DEFAULT_TEXT_COL = const.BLACK

    def __init__(self, x, y, text, type = const.buttonMode.BOOL, 
                 callback = None, args = None):
        self.x = x
        self.y = y
        self.text = text
        self.button_col = Button.DEFAULT_COL
        self.hover_col = Button.DEFAULT_HOVER_COL
        self.click_col = Button.DEFAULT_CLICK_COL
        self.text_col = Button.DEFAULT_TEXT_COL
        self.screen = None
        self._font = pygame.font.SysFont("Times New Roman", 30)
        if type == const.buttonMode.CALLBACK:
            assert callable(callback), ("callback must be a function in " 
                                        "callback mode")
        self.type = type
        self.callback = callback
        self.args = args
        self._event_type = None

        # TODO do the tags in this project

    def changeFont(self, new_font):
        self._font = new_font

    def changeColors(self, button_col, hover_col, click_col, text_col):
        self.button_col = button_col
        self.hover_col = hover_col
        self.click_col = click_col
        self.text_col = text_col

    def __executeCallBack(self):
        return self.callback(*self.args)

    def get_event(self, event):
        self._event = event

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._event_type = pygame.MOUSEBUTTONDOWN

        elif event.type == pygame.MOUSEBUTTONUP:
            self._event_type = pygame.MOUSEBUTTONUP

        else:
            self._event_type = None

    def drawButton(self, screen):
        # Need to refactor this because the name sucks 
        self.screen = screen.window
        update = False
        callbackReturn = None
        
        text_img = self._font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()

        width = max(Button.WIDTH, text_len + 10)

        button_rect = pygame.Rect(self.x, self.y, width, Button.HEIGHT)
        
            
        if self._event_type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(*self._event.pos):
                pygame.draw.rect(self.screen, self.click_col, button_rect)
                self._event_type = None
            else:
                pygame.draw.rect(self.screen, self.button_col, button_rect)
                self._event_type = None

        elif self._event_type == pygame.MOUSEBUTTONUP:
            if button_rect.collidepoint(*self._event.pos):
                 
                pygame.draw.rect(self.screen, self.button_col, button_rect)
                # execute callback function if set
                if self.type == const.buttonMode.CALLBACK:
                    callbackReturn = self.__executeCallBack()
                update = True
                self._event_type = None
            else:
                pygame.draw.rect(self.screen, self.button_col, button_rect)
                self._event_type = None

        else:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.hover_col, button_rect)
            else:
                pygame.draw.rect(self.screen, self.button_col, button_rect)

        # add text to the button
        self.screen.blit(text_img, 
                         (self.x + int(width / 2) - int(text_len / 2), 
                         self.y + 5))

        return update, callbackReturn

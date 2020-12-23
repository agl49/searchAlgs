# This contains classes related to pygame GUI creation
# This is mainly for quick and dirty ui elements.
# Use a separate module for more a more in depth GUI
# Current implementation only takes in callbacks with list
# as args
import pygame
import const


class simpleTextInput:
    # constants
    # NUMBERS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
    #            pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
    #            pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, 
    #            pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, 
    #            pygame.K_KP8, pygame.K_KP9]

    SPECIAL = [pygame.K_EXCLAIM, pygame.K_QUOTEDBL, pygame.K_HASH, 
               pygame.K_DOLLAR, pygame.K_AMPERSAND, pygame.K_QUOTE, 
               pygame.K_LEFTPAREN, pygame.K_RIGHTPAREN, pygame.K_ASTERISK,
               pygame.K_PLUS, pygame.K_COMMA, pygame.K_MINUS, pygame.K_PERIOD,
               pygame.K_SLASH, pygame.K_COLON, pygame.K_SEMICOLON, 
               pygame.K_LESS, pygame.K_GREATER, pygame.K_GREATER, pygame.K_AT,
               pygame.K_LEFTBRACKET, pygame.KSCAN_BACKSLASH,
               pygame.K_RIGHTBRACKET, pygame.K_CARET, pygame.K_UNDERSCORE, 
               pygame.K_BACKQUOTE, pygame.K_KP_PERIOD, pygame.K_KP_DIVIDE, 
               pygame.K_KP_MULTIPLY, pygame.K_KP_MINUS, pygame.K_KP_PLUS,
               pygame.K_KP_ENTER, pygame.K_KP_EQUALS]


    # Dictionary inputs
    # "x" = int pixel position on screen
    # "y" = int pixel position on screen
    # "width" = int pixel width
    # "height" = int pixel width
    # "pos" = pygame.math.Vector2(x,y) 
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
        self._bg_color = kwargs["bg_Color"]
        self._active_color = kwargs["active_color"]
        self.active = False
        self.text = ""
        self.text_size = 24 or kwargs["text_size"]
        self._font = pygame.font.SysFont("Constantia", self.text_size)
        self._text_color = kwargs["text_color"]
        self._boarder_color = kwargs["boarder_color"]
        self._boarder = kwargs["boarder"]
    
    def update(self, surface):
        # I think just having this contain all internal check function
        # would be good
        pass

    def _check_click(self):
        if self._rect.collidepoint(pygame.mouse.get_pos):
            self._active = True
        else: 
            self._active = False

    def draw(self, surface):
        # check time 39:47
        if (self._boarder == 0) and not self.active:
            self._image.fill(self._bg_color)

        elif (self._boarder == 0) and self.active:
            self._image.fill(self._active_color)

        else:
            if self.active:
                self._image.fill(self._active_color)
            else:
                self._image.fill(self._bg_color)

            pygame.draw.rect(self._image, self._boarder_color, self._rect, 
                             self._boarder)
        
        text = self._font.render(self.text, False, self._text_color)
        text_height = text.get_hight()
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

    def add_text(self, key):
        try:
            
            # Backspace
            if key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
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

            # Special char
            elif key in simpleTextInput.SPECIAL:
                text = list(self.text)
                text.append(chr(key))
                self.text = "".join(text)

            # add numbers and letters
            elif chr(key).isalnum():
                text = list(self.text)
                text.append(chr(key))
                self.text = "".join(text)

            else:
                # Key not accepted
                print(f"Key not accepted: {key}")

        except:
            # Throw exception?
            print("IO error in text box")

    def return_text(self):
        if not self.active:
            return self.text

class simpleTextLable:
    def __init__(self, text):
        self._text = text

    def set_font(self, font, font_size, color, selected_color, 
                 antialias = True):
        self._font = font
        self._font_size = font_size
        self._color = color
        self._selected_color = selected_color
        self._antialias = antialias
        # self._rect = pygame.Rect(0, 0, 0, 0)

    # This is mainly to make give flexibility to text instantiation
    def _render_font(self, text, color = (0, 0, 0)):
        assert isinstance(color, tuple), "Color is not tuple"

        return self._font.render(text, self._antialias, color)

    def _render_string(self):
        text = self._render_font(self._text, self._color)
        # not sure about this, we are creating a new surface for the
        # text then adding that surface to the window instead of adding
        # that surface to the og window. Not sure if we shoudl do it 
        # this way
        text_surface = pygame.Surface((int(text.get_width()), int(text.get_hight())), pygame.SRCALPHA, 32)
        # Making surface optimized for alpha based transparency 
        text_surface = pygame.Surface.convert_alpha(text_surface)

        # Still not sure about this...
        text_surface.blit(text, (0,0))
        # new_width = text_surface.get_size()[0]
        new_hight = text_surface.get_size()[1]

        text_surface = pygame.transform.smoothscale(text_surface, (text.get_width(), new_hight))

        return text_surface

    def draw(self, surface, pos):
        self._surface = self._render_string()
        # self._rect.width, self._rect.height = self._surface.get_size()

        surface.blit(self._surface, pos) 

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

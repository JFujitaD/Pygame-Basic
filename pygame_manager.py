from pygame.constants import K_RIGHT
from pygame.rect import Rect
from Models.pygame_text import Text
from Models.pygame_rectangle import Rectangle
from Models.pygame_image import Image
from Models.pygame_key_event import KeyEvent
import pygame
import sys
import uuid


class PygameConstants:
    """The constants used in pygame_manager"""
    FPS = 60
    WIDTH = 900
    HEIGHT = 600
    DEFAULT_BACKGROUND_COLOR = (128, 128, 128)
    DEFAULT_CAPTION = 'Pygame Manager'

class PygameKeys:
    """The constants for key pressed used in main"""
    K_W = pygame.K_w
    K_A = pygame.K_a
    K_S = pygame.K_s
    K_D = pygame.K_d

    K_UP = pygame.K_UP
    K_LEFT = pygame.K_LEFT
    K_DOWN = pygame.K_DOWN
    K_RIGHT = pygame.K_RIGHT

    M_LEFT = 1
    M_MIDDLE = 2
    M_RIGHT = 3
    
    K_SPACE = pygame.K_SPACE


class PygameColors:
    """The color constants used in main

        Source: https://www.rapidtables.com/web/color/RGB_Color.html
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    GREEN = (0, 128, 0)
    PURPLE = (128, 0, 128)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)


class PygameManager:
    def __init__(self, width=PygameConstants.WIDTH, height=PygameConstants.HEIGHT) -> None:
        """Initializes the game

            Args:
                width (optional): Width of the window.
                height (optional): Height of the window
        """
        self.rectangles = {}
        self.custom_colors = {}
        self.texts = {}
        self.images = {}
        self.key_events = {}
        self.events = {}

        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = PygameConstants.FPS
        self.clock = pygame.time.Clock()
        self.background_color = PygameConstants.DEFAULT_BACKGROUND_COLOR
        self.background_image = None

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(PygameConstants.DEFAULT_CAPTION)


    def start_game(self) -> None:
        """Starts the game loop"""
        while True:
            for event in pygame.event.get():
                # Exit button pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Left click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == PygameKeys.M_LEFT:
                    self.try_key_event(PygameKeys.M_LEFT)
                # Middle click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == PygameKeys.M_MIDDLE:
                    self.try_key_event(PygameKeys.M_MIDDLE)
                # Right click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == PygameKeys.M_RIGHT:
                    self.try_key_event(PygameKeys.M_RIGHT)
                    
            if self.background_image is None:
                self.window.fill(self.background_color)
            else:
                bg_image = pygame.image.load(self.background_image)
                self.window.blit(bg_image, (0, 0))
            
            # Iterate through all objects and draw them on screen
            keys = pygame.key.get_pressed()
            for k, v in self.key_events.items():
                if keys[k] and v.last_activated <= 0:
                    v.last_activated = v.frequency
                    v.func()
                else:
                    v.last_activated -= 1

            for event in self.events.values():
                event()

            for r in self.rectangles.values():
                py_rect = pygame.Rect(r.x, r.y, r.width, r.height)
                pygame.draw.rect(self.window, r.color, py_rect)

            for t in self.texts.values():
                font = pygame.font.SysFont(None, t.size)
                screen = font.render(t.text, True, t.color)
                self.window.blit(screen, (t.x, t.y))

            for k, v in self.images.items():
                image = pygame.image.load(v.file_path)
                self.window.blit(image, (v.x, v.y))
            
            pygame.display.update()
            self.clock.tick(self.FPS)

            
    def set_background_color(self, color) -> None:
        """Set the background color of the main window

            Args:
                color: The new background color. Use PygameColors.<color>
        """
        self.background_image = None
        self.background_color = color

    def set_background_image(self, file_path) -> None:
        """Sets the background image of the main window
        
            Args:
                file_path: The path of the image file.
        """
        self.background_image = file_path


    def draw_image(self, x, y, image_id, file_path) -> Image:
        """Draws the image on the screen
        
            Args:
                x: Position of top left corner of text.
                y: Position of top left corner of text.
                image_id: Unique id of the image.
                file_path: The path of the image file.

            Returns:
                Image: The drawn image.
        """
        image = Image(x, y, file_path)
        self.images[image_id] = image
        return image

    def get_image(self, image_id) -> Image:
        """Gets the image that has been drawn

            Args:
                image_id: Unique id of the image.

             Returns:
                Image: An image.
        """
        try:
            return self.images[image_id]
        except KeyError:
            print('Error: Image with id of "' + image_id + '" does not exist.')

    def remove_image_by_id(self, image_id) -> None:
        """Removes the image that has been created by id.

            Args:
                image_id: Unique id of the image.
        """
        del self.images[image_id]

    def remove_image_by_value(self, image) -> None:
        """Removes the image that has been created by value

            Args:
                rect: The image that needs to be removed.
        """
        for k, v in self.images.items():
            if v == image:
                del self.images[k]
                break



    def draw_rectangle(self, x, y, width, height, rect_id, color) -> Rectangle:
        """Draws a rectangle on the window

            Args: 
                x: Position of top left corner of rectangle.
                y: Position of top left corner of rectangle.
                width: Width of the rectangle.
                height: Height of the rectangle. 
                rect_id: Unique id of the rectangle.
                color: The rectangle's color. Use PygameColors.<color>

             Returns:
                Rectangle: The drawn rectangle.
        """
        rect = Rectangle(x, y, width, height, color)
        self.rectangles[rect_id] = rect
        return rect

    def get_rectangle(self, rect_id) -> Rectangle:
        """Gets the rectangle that has been created

            Args:
                rect_id: The unique id of the rectangle.
            
            Returns:
                Rectangle: The rectangle.
        """
        try:
            return self.rectangles[rect_id]
        except KeyError:
            print('Error: Rectangle with id of ' + str(rect_id) + ' does not exist.')

    def remove_rectangle_by_id(self, rect_id) -> None:
        """Removes the rectangle that has been created by the id

            Args:
                rect_id: The unique id of the rectangle.
        """
        del self.rectangles[rect_id]

    def remove_rectangle_by_value(self, rect) -> None:
        """Removes the rectangle that has been created by value

            Args:
                rect: The rectangle that needs to be removed.
        """
        for k, v in self.rectangles.items():
            if v == rect:
                del self.rectangles[k]
                break


    def create_custom_color(self, color_name, rgb) -> tuple:
        """Creates a custom color using an RGB tuple.

            Args:
                color_name: The unique name of the newly created color.
                rgb: The RGB values of the color in the form (r, g, b).
            
            Returns:
                tuple: A tuple with three values.
        """
        self.custom_colors[color_name] = rgb
        return rgb
    
    def get_custom_color(self, color_name) -> tuple:
        """Gets the custom color that has already been created
            
            Args:
                color_id: The unique name of the color that was created

            Returns:
                tuple: A tuple with three values.
        """
        try:
            return self.custom_colors[color_name]
        except KeyError:
            print('Error: Color with name of "' + color_name + '" does not exist.') 


    def draw_text(self, x, y, size, text, text_id, color) -> Text:
        """Draws text on the screen

            Args:
                x: Position of top left corner of text.
                y: Position of top left corner of text.
                size: The font size.
                text: The text you want to display.
                text_id: The unique id of the text
                color: The color of the text

            Returns:
                Text: The drawn text.
        """
        layer = Text(x, y, size, text, color)
        self.texts[text_id] = layer
        return layer

    def get_text(self, text_id) -> Text:
        """Gets the text that has been created
        
            Args:
                text_id: The unique id of the text

            Returns:
                Text: The text.
        """
        try:
            return self.texts[text_id]
        except KeyError:
            print('Error: Text with id of ' + str(text_id) + ' does not exist.')


    def add_key_event(self, key, func, frequency=None) -> None:
        """Adds an event listener for the specified key, and assigns a function to the key
        
            Args:
                key: The key that activates the function. Use PygameKeys.<key>
                func: The function that should run when the key is pressed.
                frequency: The number of times the function is executed per second. DOES NOT WORK WITH MOUSE EVENTS.
        """
        if frequency is None:
            self.key_events[key] = KeyEvent(func, 0)
        else:
            self.key_events[key] = KeyEvent(func, frequency)

    def try_key_event(self, key) -> None:
        """Tries to execute the function of the key event with given key
        
            Args:
                key: The key that activates this event.
        """
        try:
            self.key_events[key].func()
        except KeyError:
            print('Error: Key event with the given key does not exist.')

    def add_event(self, event_id, func) -> None:
        """Adds an event that is run every game tick
        
            Args:
                event_id: The unique id for the event.
                func: The function that should run every game tick.
        """
        self.events[event_id] = func


    def is_on_screen(self, object, remove=False) -> bool:
        """Checks if the given rectangle or image is completely off of the screen
        
            Args:
                object: The rectangle or image.
                remove: If true, remove the given rectangle or image.
            
            Returns:
                bool: True if the given rect is on the screen.
        """
        object_type = type(object)

        if not (object.x + object.width > 0 and object.x < self.WIDTH):
            if object_type == Rectangle:
                self.remove_rectangle_by_value(object)
            else:
                self.remove_image_by_value(object)
            return False
        if not (object.y + object.height > 0 and object.y < self.HEIGHT):
            if object_type == Rectangle:
                self.remove_rectangle_by_value(object)
            else:
                self.remove_image_by_value(object)
            return False
        return True
    
    def move_left(self, object, speed, check=False) -> None:
        """Tries to move the object to the left.
        
            Args:
                object: Rectangle or image.
                speed: The speed to move the object
                check: Determins whether or not to check if the object will go off the screen
        """
        if check:
            if object.x > 0:
                object.x -= speed
        else:
            object.x -= speed
        
    def move_right(self, object, speed, check=False) -> None:
        """Tries to move the object to the right.
        
            Args:
                object: Rectangle or image.
                speed: The speed to move the object
                check: Determins whether or not to check if the object will go off the screen
        """
        if check:
            if object.x + object.width < self.WIDTH:
                object.x += speed
        else:
            object.x += speed

    def move_up(self, object, speed, check=False) -> None:
        """Tries to move the object up.
        
            Args:
                object: Rectangle or image.
                speed: The speed to move the object
                check: Determins whether or not to check if the object will go off the screen
        """
        if check:
            if object.y > 0:
                object.y -= speed
        else:
            object.y -= speed

    def move_down(self, object, speed, check=False) -> None:
        """Tries to move the object down.
        
            Args:
                object: Rectangle or image.
                speed: The speed to move the object
                check: Determins whether or not to check if the object will go off the screen
        """
        if check:
            if object.y + object.height < self.HEIGHT:
                object.y += speed
        else:
            object.y += speed

    
    def get_uuid(self) -> int:
        """Returns a universally unique identifier, A.K.A. a unique integer
        
            Returns:
                int: The universally unique identifier (UUID).    
        """
        return uuid.uuid4().int
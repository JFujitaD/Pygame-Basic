from pygame_rectangle import Rectangle
import pygame
import sys


class PygameConstants:
    """The constants used in pygame_manager"""
    FPS = 60
    WIDTH = 900
    HEIGHT = 600
    DEFAULT_BACKGROUND_COLOR = (128, 128, 128)

class PygameColors:
    """The color constants used in main"""
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


class PygameManager:
    def __init__(self, width=PygameConstants.WIDTH, height=PygameConstants.HEIGHT):
        """Initializes the game

            Args:
                width (optional): Width of the window.
                height (optional): Height of the window
        """
        self.rectangles = []
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = PygameConstants.FPS
        self.clock = pygame.time.Clock()
        self.background = PygameConstants.DEFAULT_BACKGROUND_COLOR

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Pygame Manager')

    def start_game(self):
        """Starts the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            # TODO Game logic
            self.window.fill(self.background)

            for r in self.rectangles:
                py_rect = pygame.Rect(r.x, r.y, r.width, r.height)
                pygame.draw.rect(self.window, r.color, py_rect)
            
            pygame.display.update()
            self.clock.tick(self.FPS)

    def set_background_color(self, color):
        """Set the background of the main window

            Args:
                color: The new background color. Use PygameColors.<color>
        """
        self.background = color

    def draw_rectangle(self, x, y, width, height, color):
        """Draws a rectangle on the window

            Args: 
                x: Position of top left corner of rectangle.
                y: Position of top left corner of rectangle.
                width: Width of the rectangle.
                height: Height of the rectangle. 
                color: The rectangle's color. Use PygameColors.<color>

        """
        rect = Rectangle(x, y, width, height, color)
        self.rectangles.append(rect)
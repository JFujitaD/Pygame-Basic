import pygame
import sys
import pygame_constants as constants


class PygameManager:
    def __init__(self, width=constants.WIDTH, height=constants.HEIGHT):
        """Initializes the game

            Args:
                width (optional): Width of the window.
                height (optional): Height of the window
        """
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = constants.FPS
        self.clock = pygame.time.Clock()

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
            
            pygame.display.update()
            self.clock.tick(self.FPS)
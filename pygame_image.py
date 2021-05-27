class Image:
    def __init__(self, x, y):
        """A custom implementation of pygame.image that only holds x and y coordinates
        
            Args:
                x: Position of top left corner of image.
                y: Position of top left corner of image.
        """
        self.x = x
        self.y = y
    
    def __str__(self):
        representation = 'T: Image X: ' + str(self.x) + ' Y: ' + str(self.y)
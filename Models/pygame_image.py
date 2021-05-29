from pygame import image


class Image:
    """A custom implementation of pygame.image that only holds x and y coordinates"""
    def __init__(self, x, y, file_path) -> None:
        """Creates a new Image
        
            Args:
                x: Position of top left corner of image.
                y: Position of top left corner of image.
                file_path: The path of the image file.
        """
        self.x = x
        self.y = y

        img = image.load(file_path)
        self.width = img.get_size()[0]
        self.height = img.get_size()[1]
    
    def __str__(self) -> str:
        representation = 'T: Image X: ' + str(self.x) + ' Y: ' + str(self.y)
        return representation
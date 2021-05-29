class Rectangle:
    """A custom implementation for pygame.Rect that holds a color"""
    def __init__(self, x, y, width, height, color) -> None:
        """Creates a new instance of Rectangle

            Args: 
                x: Position of top left corner of rectangle.
                y: Position of top left corner of rectangle.
                width: Width of the rectangle.
                height: Height of the rectangle. 
                color: The rectangle's color. Use PygameColors.<color>
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def __str__(self) -> str:
        representation = 'X: ' + str(self.x) + ' Y:' + str(self.y)
        representation += '\nW: ' + str(self.width) + ' H: ' + str(self.height)
        representation += '\nC: ' + str(self.color)

        return representation
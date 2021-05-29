class Text:
    """A custom implementation for pygame.text that holds a coordinate"""
    def __init__(self, x, y, size, text, color):
        """Creates a new instance of Text

            Args: 
                x: Position of top left corner of text.
                y: Position of top left corner of text.
                size:  Font size of text.
                color: The text's color. Use PygameColors.<color>
        """
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color

    def __str__(self):
        representation = 'X: ' + str(self.x) + ' Y:' + str(self.y)
        representation += '\nS: ' + str(self.size) + " T: " + self.text
        representation += '\nC: ' + str(self.color)

        return representation

import pygame_manager

class KeyEvent:
    """A wrapper class for an event to encapsulate delay time"""
    def __init__(self, func, frequency) -> None:
        """Creates a key event
        
            Args:
                func: The function that should be executed.
                frequency: The number of times the function is executed per second.
        """
        self.func = func

        if frequency == 0:
            self.frequency = 0
        else:
            self.frequency =  pygame_manager.PygameConstants.FPS / frequency

        self.last_activated = 0
        
class KeyEvent:
    """A wrapper class for an event to encapsulate delay time"""
    def __init__(self, func, delay):
        """Creates a key event
        
            Args:
                func: The function that should be executed.
                delay: The delay between function execution.
        """
        self.func = func
        self.delay = delay
        self.last_activated = 0
        
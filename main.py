from pygame_manager import PygameManager


def main():
    """Entry point for program that tests the PygameManager

        1. pm = PygameManager()
        2. pm.start_game()
    """
    pm = PygameManager()
    pm.set_background_color((255, 255, 0))
    pm.start_game()


if __name__ == '__main__':
    main() 
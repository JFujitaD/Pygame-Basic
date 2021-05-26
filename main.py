from pygame_manager import PygameManager, PygameColors


def main():
    """Entry point for program that tests the PygameManager

        1. pm = PygameManager()
        2. pm.start_game()
    """
    pm = PygameManager()

    pm.set_background_color(PygameColors.BLACK)
    pm.draw_rectangle(10, 10, 100, 80, PygameColors.RED)

    pm.start_game()


if __name__ == '__main__':
    main() 
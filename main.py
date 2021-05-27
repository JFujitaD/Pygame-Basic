from pygame_manager import PygameManager, PygameColors


def main():
    """Entry point for program that tests the PygameManager

        Instructions: 
            1. pm = PygameManager()
            2. # Add your own code here
            3. pm.start_game()
    """

    pm = PygameManager()

    pm.set_background_color(PygameColors.NAVY)
    pm.draw_rectangle(10, 10, 100, 80, 1, PygameColors.PURPLE)

    pm.create_custom_color('gold', (255, 215, 0))
    pm.draw_rectangle(80, 50, 10, 20, 2, pm.get_custom_color('gold'))

    print(pm.get_rectangle(2))

    pm.draw_text(100, 100, 24, 'Hello World!', 1, PygameColors.MAROON)
    print(pm.get_text(1))

    pm.start_game()


if __name__ == '__main__':
    main() 
from pygame_manager import PygameManager, PygameColors


def main():
    """Entry point for program that tests the PygameManager

        Instructions: 
            1. pm = PygameManager()
            2. # Add your own code here
            3. pm.start_game()
    """

    pm = PygameManager()

    pm.set_background_color(PygameColors.BLACK)
    pm.draw_rectangle(10, 10, 100, 80, 'red_rect', PygameColors.RED)

    pm.create_custom_color('yellow', (255, 255, 0))
    pm.draw_rectangle(80, 50, 10, 20, 'yellow_rect', pm.get_custom_color('yellow'))

    print(pm.get_rectangle('yellow_rect'))

    pm.start_game()


if __name__ == '__main__':
    main() 
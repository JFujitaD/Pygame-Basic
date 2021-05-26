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
    pm.draw_rectangle(10, 10, 100, 80, 'red_rect', PygameColors.PURPLE)

    pm.create_custom_color('gold', (255, 215, 0))
    pm.draw_rectangle(80, 50, 10, 20, 'gold_rect', pm.get_custom_color('gold'))

    print(pm.get_rectangle('gold_rect'))

    pm.start_game()


if __name__ == '__main__':
    main() 
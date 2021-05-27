from pygame_manager import PygameManager, PygameColors


def main():
    """Entry point for program that tests the PygameManager

        Instructions: 
            1. pm = PygameManager()
            2. # Add your own code here
            3. pm.start_game()
    """

    pm = PygameManager(500, 500)

    pm.set_background_color(PygameColors.GRAY)

    pm.create_custom_color('gold', (255, 215, 0))
    gold = pm.get_custom_color('gold')
    

    pm.draw_rectangle(25, 25, 450, 450, 1, gold)
    pm.draw_text(30, 30, 50, 'Pygame Demo', 1, PygameColors.BLACK)
    pm.draw_text(30, 70, 40, 'Smoll Text', 2, PygameColors.NAVY)

    pm.start_game()


if __name__ == '__main__':
    main() 
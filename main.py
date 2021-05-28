from pygame_manager import PygameManager, PygameColors, PygameKeys


def main():
    """Entry point for program that tests the PygameManager

        Instructions: 
            1. from pygame_manager import PygameManager, PygameColors, PygameKeys
            2. pm = PygameManager()
            3. # Add your own code here
            4. pm.start_game()
    """

    pm = PygameManager(500, 500)

    pm.set_background_color(PygameColors.GRAY)

    pm.create_custom_color('gold', (255, 215, 0))
    gold = pm.get_custom_color('gold')
    
    pm.draw_rectangle(25, 25, 450, 450, 1, gold)
    pm.draw_text(40, 40, 50, 'Pygame Demo', 1, PygameColors.BLACK)
    pm.draw_text(45, 80, 40, 'Smoll Text', 2, PygameColors.NAVY)
    pm.draw_image(50, 150, 'Images/pygame.png')

    def w_key_pressed():
        print('W key was pressed')
    pm.add_key_event(PygameKeys.K_W, w_key_pressed)

    pm.start_game()


if __name__ == '__main__':
    main() 
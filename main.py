from pygame_manager import PygameManager, PygameColors, PygameKeys


def main():
    """Entry point for program that demonstrates PygameManager

        Instructions: 
            1. from pygame_manager import PygameManager, PygameColors, PygameKeys
            2. pm = PygameManager()
            3. # Add your own code here
            4. pm.start_game()
    """

    # Initializing the game
    pm = PygameManager(500, 500)

    # Setting the background image
    pm.set_background_image('Images/space_500.png')

    # Creating a custom color
    pm.create_custom_color('gold', (255, 215, 50))
    gold = pm.get_custom_color('gold')
    
    # Drawing a rectangle
    pm.draw_rectangle(25, 25, 450, 450, 1, gold)

    # Drawing text
    pm.draw_text(40, 40, 50, 'Pygame Demo', 1, PygameColors.BLACK)
    pm.draw_text(45, 80, 40, 'Smoll Text', 2, PygameColors.NAVY)

    # Drawing an image
    snake = pm.draw_image(50, 150, pm.get_uuid(), 'Images/pygame.png')

    # Adding a key event
    def a_key_pressed():
        snake.x -= 0.5
    pm.add_key_event(PygameKeys.K_A, a_key_pressed)
    
    def d_key_pressed():
        snake.x += 0.5
    pm.add_key_event(PygameKeys.K_D, d_key_pressed)

    # Starting the game
    pm.start_game()


if __name__ == '__main__':
    main() 
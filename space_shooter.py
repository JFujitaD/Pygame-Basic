from pygame import image
from pygame_manager import PygameManager, PygameColors, PygameKeys
import random

pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 'Images/penguin.png')
spaceship = pm.get_image('Images/penguin.png')
speed = 3

def spaceship_left():
    pm.move_left(spaceship, speed, True)
pm.add_key_event(PygameKeys.K_A, spaceship_left)

def spaceship_right():
    pm.move_right(spaceship, speed, True)
pm.add_key_event(PygameKeys.K_D, spaceship_right)

def spaceship_up():
    pm.move_up(spaceship, speed, True)
pm.add_key_event(PygameKeys.K_W, spaceship_up)

def spaceship_down():
    pm.move_down(spaceship, speed, True)
pm.add_key_event(PygameKeys.K_S, spaceship_down)


bullets = []

def fire_bullet():
    pm.draw_rectangle(spaceship.x - 1 + spaceship.width / 2, spaceship.y - 10, 2, 10, len(bullets), PygameColors.RED)
    bullets.append(pm.get_rectangle(len(bullets)))
pm.add_key_event(PygameKeys.K_SPACE, fire_bullet)

def move_bullet():
    for bullet in bullets:
        pm.move_up(bullet, speed, False)
        if not pm.is_on_screen(bullet, True):
            bullets.remove(bullet)
    print(len(pm.rectangles))

pm.add_event(1, move_bullet)


pm.start_game()
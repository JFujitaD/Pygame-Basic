from pygame_manager import PygameManager, PygameColors, PygameKeys

# Setup
pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

spaceship = pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 'Images/spaceship.png')
speed = 3

# Asteroids
pm.draw_image(10, 10, 'Images/asteroid_64.png')
pm.draw_image(600, 100, 'Images/asteroid_128.png')
pm.draw_image(300, 200, 'Images/asteroid_96.png')

# Movement controls
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


# Firing mechanics
bullets = []

def fire_bullet():
    uuid = pm.get_uuid()
    bullets.append(pm.draw_rectangle(spaceship.x - 1 + spaceship.width / 2, spaceship.y - 10, 2, 10, uuid, PygameColors.RED))
pm.add_key_event(PygameKeys.K_SPACE, fire_bullet, 5)

def move_bullet():
    for bullet in bullets:
        pm.move_up(bullet, speed, False)
        if not pm.is_on_screen(bullet, True):
            bullets.remove(bullet)

pm.add_event(1, move_bullet)


# Start game
pm.start_game()
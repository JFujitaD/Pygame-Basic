from pygame_manager import PygameManager, PygameColors, PygameKeys

# Setup
pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

spaceship = pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 1, 'Images/spaceship.png')
speed = 3

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
ammo = []

def fire_laser():
    uuid = pm.get_uuid()
    x = spaceship.x + (spaceship.width / 2)
    y = spaceship.y

    laser = pm.draw_image(x, y, uuid, 'Images/laser_small.png')
    laser.x -= laser.width / 2
    laser.y -= laser.height

    ammo.append(laser)
pm.add_key_event(PygameKeys.M_LEFT, fire_laser)

def fire_bomb():
    uuid = pm.get_uuid()
    x = spaceship.x + (spaceship.width / 2)
    y = spaceship.y

    bomb = pm.draw_image(x, y, uuid, 'Images/bomb_small.png')
    bomb.x -= bomb.width / 2
    bomb.y -= bomb.height

    ammo.append(bomb)
pm.add_key_event(PygameKeys.M_RIGHT, fire_bomb)

def move_ammo():
    for a in ammo:
        pm.move_up(a, speed, False)
        if not pm.is_on_screen(a, True):
            ammo.remove(a)

pm.add_event(1, move_ammo)


# Start game
pm.start_game()
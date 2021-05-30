from pygame_manager import PygameManager, PygameColors, PygameKeys
import random

# Setup
pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

spaceship = pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 1, 'Images/spaceship.png')
speed = 3
maximum_ammo = 5


# Text
score = pm.draw_text(5, 5, 64, 'Score: 0', 1, PygameColors.WHITE)
asteroids_destroyed = 0

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
    if len(ammo) < maximum_ammo:
        uuid = pm.get_uuid()
        x = spaceship.x + (spaceship.width / 2)
        y = spaceship.y

        laser = pm.draw_image(x, y, uuid, 'Images/laser_small.png')
        laser.x -= laser.width / 2
        laser.y -= laser.height

        ammo.append(laser)
pm.add_key_event(PygameKeys.M_LEFT, fire_laser)

def move_ammo():
    for a in ammo:
        pm.move_up(a, speed, False)
        if not pm.is_on_screen(a, True):
            ammo.remove(a)

pm.add_event(1, move_ammo)


# Asteroids
asteroids = []

def spawn_asteroids():
    if random.random() < 0.07:
        size = random.randint(0, 2)
        image = ''

        if size == 0:
            image = 'Images/asteroid_64.png'
        elif size == 1:
            image = 'Images/asteroid_96.png'
        else:
            image = 'Images/asteroid_128.png'

        x = random.randint(0, pm.WIDTH)
        asteroid = pm.draw_image(x, -150, pm.get_uuid(), image)
        asteroid.y = -asteroid.height
        asteroids.append(asteroid)

    for asteroid in asteroids:
        asteroid.y += speed
        if not pm.is_on_screen(asteroid, True):
            asteroids.remove(asteroid)
pm.add_event(2, spawn_asteroids)


# Collisions
def bullet_asteroid_collision():
    for a in ammo:
        for asteroid in asteroids:
            if pm.check_collision(a, asteroid):
                global asteroids_destroyed
                asteroids_destroyed += 1
                score.text = 'Score: ' + str(asteroids_destroyed)

                pm.remove_image_by_value(a)
                ammo.remove(a)
                pm.remove_image_by_value(asteroid)
                asteroids.remove(asteroid)
pm.add_event(3, bullet_asteroid_collision)

def player_asteroid_collision():
    for asteroid in asteroids:
        if pm.check_collision(spaceship, asteroid):
            pm.stop_game(True)
            pm.draw_text(215, 300, 100, 'Game Over', pm.get_uuid(), PygameColors.RED)
pm.add_event(4, player_asteroid_collision)
            

# Start game
pm.start_game()
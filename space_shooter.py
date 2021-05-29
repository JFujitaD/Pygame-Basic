from pygame_manager import PygameManager, PygameColors, PygameKeys

pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 'Images/spaceship.png')
spaceship = pm.get_image('Images/spaceship.png')
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


pm.start_game()
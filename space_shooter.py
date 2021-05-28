from pygame_manager import PygameManager, PygameColors, PygameKeys

pm = PygameManager(800, 800)

pm.set_background_image('Images/space_800.png')

pm.draw_image(pm.WIDTH/2, pm.HEIGHT/2, 'Images/spaceship.png')
spaceship = pm.get_image('Images/spaceship.png')
speed = 3

def spaceship_up():
    spaceship.y -= speed
pm.add_key_event(PygameKeys.K_W, spaceship_up)

def spaceship_down():
    spaceship.y += speed
pm.add_key_event(PygameKeys.K_S, spaceship_down)

def spaceship_left():
    spaceship.x -= speed
pm.add_key_event(PygameKeys.K_A, spaceship_left)

def spaceship_right():
    spaceship.x += speed
pm.add_key_event(PygameKeys.K_D, spaceship_right)

pm.start_game()
from pygame_manager import PygameManager, PygameColors, PygameKeys
import time

# Initialize the game
width = 500
height = 900
animation_delay = 0.25
tower_built = False
pm = PygameManager(width, height)
pm.set_background_image('Images/tower_background.png')
start_text = pm.draw_text(110, 475, 32, 'Press "Left Click" to build.', pm.get_uuid(), PygameColors.BLACK)

# Create the floors for the tower
tower = {'floors': [], 'width': 400, 'height': 100, 'font_size': 24}

tower['floors'].append({'name': 'Sushi Restaurant', 'color': PygameColors.RED})
tower['floors'].append({'name': 'Party Apartments', 'color': PygameColors.YELLOW})
tower['floors'].append({'name': 'Scoops Ice Cream', 'color': PygameColors.GREEN})
tower['floors'].append({'name': 'Carmine Apartments', 'color': PygameColors.BLUE})


def build_tower():
    global tower_built
    if not tower_built:
        tower_built = True
        start_text.text = ''

        # For each floor in the tower, draw the components.
        x = width - tower['width']
        y = height - tower['height']
        for i, floor in enumerate(tower['floors']):
            pm.draw_rectangle(x, y, tower['width'], tower['height'], i, floor['color'])

            pm.draw_text(x+5, y+5, tower['font_size'], floor['name'], pm.get_uuid(), PygameColors.BLACK)
            pm.draw_text(x+5, y+tower['font_size'], tower['font_size'], 'Floor #' + str(i + 1),
                pm.get_uuid(), PygameColors.BLACK)

            y -= tower['height']

        # Elevator
        floor_count = len(tower['floors'])
        tower_height = tower['height'] * floor_count

        x = 0
        y = height - tower_height
        pm.draw_rectangle(x, y, width-tower['width'], tower_height, pm.get_uuid(),PygameColors.NAVY)
        pm.draw_rectangle(x+5, y+5, 10, tower_height-10, pm.get_uuid(), PygameColors.SILVER)
        pm.draw_rectangle(width-tower['width']-15, y+5, 10, tower_height-10, pm.get_uuid(), PygameColors.SILVER)
    else:
        print('Tower is already built.')
pm.add_key_event(PygameKeys.M_LEFT, build_tower)

# Start game
pm.start_game()
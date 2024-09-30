from pico2d import *

open_canvas()

background = load_image('TUK_GROUND.png')
character = load_image('character.png')

running = True
x = 20
y = 150
frame = 0
dir_x = 0
dir_y = 0
focusing_direction = 'right'
moving = False


def handle_events():
    global running, dir_x, dir_y, focusing_direction, moving

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            moving = True
            if event.key == SDLK_RIGHT:
                dir_x += 10
                focusing_direction = 'right'
            elif event.key == SDLK_LEFT:
                dir_x -= 10
                focusing_direction = 'left'
            elif event.key == SDLK_UP:
                dir_y += 10
                focusing_direction = 'up'
            elif event.key == SDLK_DOWN:
                dir_y -= 10
                focusing_direction = 'down'
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            is_moving = False
            if event.key == SDLK_RIGHT:
                dir_x -= 10
            elif event.key == SDLK_LEFT:
                dir_x += 10
            elif event.key == SDLK_UP:
                dir_y -= 10
            elif event.key == SDLK_DOWN:
                dir_y += 10

while running:
    clear_canvas()
    background.draw_to_origin(0, 0, 800, 600)

    if moving:
        frame = (frame + 1) % 4
    else:
        frame = 0

    if x + dir_x > 800:
        x = 800
    elif x + dir_x < 0:
        x = 0
    else:
        x += dir_x

    if y + dir_y > 600:
        y = 600
    elif y + dir_y < 0:
        y = 0
    else:
        y += dir_y

    if moving:
        if focusing_direction == 'up':
            character.clip_draw(frame * 64, 0, 64, 64, x, y)
        elif focusing_direction == 'down':
            character.clip_draw(frame * 64, 192, 64, 64, x, y)
        elif focusing_direction == 'right':
            character.clip_draw(frame * 64, 64, 64, 64, x, y)
        elif focusing_direction == 'left':
            character.clip_composite_draw(frame * 64, 64, 64, 64, 0, 'h', x, y, 64, 64)

    else:
        if focusing_direction == 'up':
            character.clip_draw(0, 0, 64, 64, x, y)
        elif focusing_direction == 'down':
            character.clip_draw(0, 192, 64, 64, x, y)
        elif focusing_direction == 'right':
            character.clip_draw(0, 64, 64, 64, x, y)
        elif focusing_direction == 'left':
            character.clip_composite_draw(0, 64, 64, 64, 0, 'h', x, y, 64, 64)

    update_canvas()
    handle_events()

    delay(0.1)

close_canvas()

import math
import pygame
import random
import sys

PANEL_SIZE = 16
SCREEN_SIZE = 3 * PANEL_SIZE
SHAPE_SIZE = 10

from pharmacontroller import PharmaScreen

def draw_square(image, size):
    x = 3
    y = 19
    for i in range(size):
        for j in range(size):
            image[y + i][x + j] = 1.0

def draw_circle(image, size):
    x = 40
    y = 23
    radius = size // 2
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            if math.sqrt(i ** 2 + j ** 2) <= radius:
                image[y + i][x + j] = 1.0

def draw_triangle(image, size):
    x = 23
    y = 3
    for i in range(size):
        half = math.ceil(i / 2)
        for j in range(-half, half + 1):
            image[y + i][x + j] = 1.0

def draw_xlogo(image, size):
    x = 19
    y = 35 
    for i in range(size):
        image[y + i][x + i] = 1.0
        image[y + i][x + size - i - 1] = 1.0

def clear_screen():
    return [[0.0 for _ in range(SCREEN_SIZE)] for _ in range(SCREEN_SIZE)]

def main():
    pygame.init()
    pygame.mixer.init()
    screen = PharmaScreen()

    print("Press 1 for square, 2 for circle, 3 for triangle, 4 for xlogo")

    # Paramètres
    shape_functions = {
        'square': draw_square,
        'circle': draw_circle,
        'triangle': draw_triangle,
        'xlogo': draw_xlogo
    }
    shapes = [*shape_functions.keys()]
    sequence = []
    user_sequence = []
    current_index = 0
    showing_sequence = True
    add_shape = True

    sounds = {
        'square': pygame.mixer.Sound('simon_sounds/simonSound1.mp3'),
        'circle': pygame.mixer.Sound('simon_sounds/simonSound2.mp3'),
        'triangle': pygame.mixer.Sound('simon_sounds/simonSound3.mp3'),
        'xlogo': pygame.mixer.Sound('simon_sounds/simonSound4.mp3')
    }

    key_map = {
        pygame.K_1: ('square', 'square'),
        pygame.K_2: ('circle', 'circle'),
        pygame.K_3: ('triangle', 'triangle'),
        pygame.K_4: ('xlogo', 'xlogo')
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not showing_sequence:
                if event.key in key_map:
                    shape, sound_key = key_map[event.key]
                    user_sequence.append(shape)
                    sounds[sound_key].play()
                    image = clear_screen()
                    shape_functions[shape](image, SHAPE_SIZE)
                    screen.set_image(image)
                pygame.time.delay(500)


                if len(user_sequence) <= len(sequence):
                    if user_sequence[-1] != sequence[len(user_sequence) - 1]:
                        print("Game Over! The correct sequence was:", sequence)
                        pygame.quit()
                        sys.exit()

                if len(user_sequence) == len(sequence):
                    if user_sequence == sequence:
                        add_shape = True
                    user_sequence = []
                    current_index = 0
                    showing_sequence = True

        if showing_sequence:
            if add_shape:
                sequence.append(random.choice(shapes))
                add_shape = False

            image = clear_screen()
            shape = sequence[current_index]
            shape_functions[shape](image, SHAPE_SIZE)
            sounds[shape].play()
            screen.set_image(image)
            pygame.time.delay(500)
            current_index += 1

            if current_index == len(sequence):
                showing_sequence = False
        else:
            image = clear_screen()
            screen.set_image(image)
            pygame.time.delay(500)

if __name__ == '__main__':
    main()

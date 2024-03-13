# date: 08. march 2024

import pygame
import random
from spawnobject import SpawnObject, FPS
import librosa
from pygame import mixer
import time

pygame.init()

# color for FPS clock
BLACK = (0, 0, 0)
# colors for screen (GREY) and grid (DARKER GREY)
GREY = (225, 225, 225)
DARKER_GREY = (222, 222, 222)
# colors for objects
YELLOW = (200, 200, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
# define screen
WIDTH, HEIGHT = 1280, 720
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_grid(positions):
    for position in positions:
        col, row, color = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, color, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, DARKER_GREY, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, DARKER_GREY, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()
    positions_wo_colors = {(pos[0], pos[1]) for pos in positions}

    # calculate if existing position still exists in next step
    # rule 1: a cell deactivates if it has less than 2 or more than 3 active neighbors
    # rule 2: a cell stays active if it has 2 or 3 active neighbors
    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors_wo_colors = {(neigh[0], neigh[1]) for neigh in neighbors}
        common_neighbors = positions_wo_colors & neighbors_wo_colors

        if len(common_neighbors) in [2, 3]:
            new_positions.add(position)

    new_positions_wo_colors = [pos[:2] for pos in new_positions]

    # Create a dictionary to store unique positions as keys and their corresponding colors as values
    position_colors = {}
    for neigh in all_neighbors:
        position_key = tuple(neigh[:2])
        color = neigh[2]
        if position_key not in position_colors:
            position_colors[position_key] = [color]
        else:
            position_colors[position_key].append(color)

    # Update position colors with the average color
    for key, colors in position_colors.items():
        if colors and len(colors) > 1:
            # Calculate average color using NumPy
            color_average = tuple(int(sum(channel) / len(colors)) for channel in zip(*colors))
            position_colors[key] = color_average

    # calculate if non-existing position will exist in next step
    # rule 3: a deactivated cell will activate if it has 3 active neighbors
    for position in all_neighbors:
        if position[:2] not in new_positions_wo_colors:
            neighbors = get_neighbors(position)

            neighbors_wo_colors = {(neigh[0], neigh[1]) for neigh in neighbors}
            common_neighbors = positions_wo_colors & neighbors_wo_colors

            if len(common_neighbors) == 3:
                if position_colors[position[:2]] and position_colors[position[:2]][0] != position[2]:
                    position = (position[0], position[1], position_colors[position[:2]])
                new_positions.add(position)

    return new_positions


def get_neighbors(pos):
    x, y, color = pos
    neighbors = set()
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.add((x + dx, y + dy, color))
    
    return neighbors


# load audio and return detected tempo and beats
def detect_beats(audio):
    y, sr = librosa.load(audio)
    o_env = librosa.onset.onset_strength(y=y, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beats = [round(x, 1) for x in times[beats]]
    return beats, tempo


# create a random RGB tuple
def random_color():
    return tuple(random.sample(range(100, 150), 3))


def main():
    # init game as running
    running = True
    playing = True
    # init counter
    count = 0
    stream_time = 0
    # init fps clock
    fps = FPS(BLACK)
    # set anticipated framerate
    framerate = 30
    # select audio
    audio = "audio/doiwannaknow.mp3"
    # get bpm(tempo) and time where beat occurs (as list of timepoints)
    beats, tempo = detect_beats(audio)
    # play music
    mixer.music.load(audio)
    mixer.music.play()
    # screen updates should fit to beat so adjust update frequency
    # fps = bpm * 0.01667
    update_freq = int(round((framerate/(tempo*0.01667))/4, 0))
    # init positions as empty set
    positions = set()

    while running:
        fps.clock.tick(framerate)

        if playing:
            count += 1
        
        if count >= update_freq:
            start = time.time()
            count = 0
            positions = adjust_grid(positions)
            end = time.time()
            duration = round(end - start, 6)
            print('num positions: ', len(positions),' duration: ', duration)
            # if processing takes to long the fps drops
            # so remove some of the positions to decrease calculation
            if duration > 0.03:
                num = int(0.5*len(positions))
                [positions.pop() for n in range(num)]

        pygame.display.set_caption("Playing" if playing else "Paused")

        # get current streaming time and compare to last one
        # if current streaming time greater and time is in list of detected beats
        # create object at a random position (but not at border)
        last_stream_time = stream_time
        stream_time = round(pygame.mixer.music.get_pos() / 1000, 1)
        if stream_time > last_stream_time and stream_time in beats:
            start_position = (random.randint(int(0.05*GRID_WIDTH), int(0.95*GRID_WIDTH)),
                              random.randint(int(0.05*GRID_HEIGHT), int(0.95*GRID_HEIGHT)))
            obj = SpawnObject(start_position, random_color()).matrix_table()
            for position in obj:
                positions.add(position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                start_position = (col, row)
                new_object = SpawnObject(start_position, RED).matrix_block()
                for position in new_object:
                    positions.add(position)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                
                if event.key == pygame.K_c:
                    positions = set()

                if event.key == pygame.K_s:
                    start_position = (random.randint(0, GRID_WIDTH), random.randint(0, GRID_HEIGHT))
                    glider = SpawnObject(start_position, GREEN).matrix_glider()
                    for position in glider:
                        positions.add(position)

                if event.key == pygame.K_a:
                    start_position = (random.randint(0, GRID_WIDTH), random.randint(0, GRID_HEIGHT))
                    pento = SpawnObject(start_position, GREEN).matrix_rpentomino()
                    for position in pento:
                        positions.add(position)

                ### test keys ###
                if event.key == pygame.K_t:
                    new_object = {(50, 50, RED), (51, 50, RED), (51, 51, GREEN), (50, 51, GREEN)}
                    for position in new_object:
                        positions.add(position)

                if event.key == pygame.K_r:
                    new_object = {(50, 50, RED), (51, 51, GREEN), (51, 52, RED), (50, 52, GREEN), (49, 52, GREEN)}#, (51, 51, GREEN), (50, 51, GREEN)}
                    for position in new_object:
                        positions.add(position)
                ######
         
        screen.fill(GREY)
        draw_grid(positions)
        fps.render(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

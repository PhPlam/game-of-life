# date: 06. march 2024

import pygame
import random
from spawnobject import SpawnObject, FPS
import librosa
from pygame import mixer

pygame.init()

# color for FPS clock
BLACK = (0, 0, 0)
# colors for screen (GREY) and grid (DARKER GREY)
GREY = (180, 180, 180)
DARKER_GREY = (178, 178, 178)
# colors for objects
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# define screen
WIDTH, HEIGHT = 1280, 720
TILE_SIZE = 5
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

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))
        # works but slow
        #neighbors = list(filter(lambda x: x in [pos[:2] for pos in positions], [neigh[:2] for neigh in neighbors]))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)
    
    for position in all_neighbors:
        neighbors = get_neighbors(position)
        
        neighbors = list(filter(lambda x: x in positions, neighbors))
        # works but slow
        #neighbors = list(filter(lambda x: x in [pos[:2] for pos in positions], [neigh[:2] for neigh in neighbors]))

        if len(neighbors) == 3:
            new_positions.add(position)
    
    return new_positions


def get_neighbors(pos):
    x, y, color = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy, color))
    
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
    return tuple(random.sample(range(256), 3))


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
    framerate = 120
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
            count = 0
            positions = adjust_grid(positions)

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
                glider = SpawnObject(start_position, GREEN).matrix_glider()
                for position in glider:
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
         
        screen.fill(GREY)
        draw_grid(positions)
        fps.render(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

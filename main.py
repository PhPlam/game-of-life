# date: 06. march 2024

import pygame
import random
from spawnobject import SpawnObject, FPS
import librosa
from pygame import mixer

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
DARKER_GREY = (126, 126, 126)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 1920, 1080
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


def detect_beats(audio):
    y, sr = librosa.load(audio)
    o_env = librosa.onset.onset_strength(y=y, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    _, beats = librosa.beat.beat_track(y=y, sr=sr)
    beats = [round(x, 2) for x in times[beats]]
    return beats


def main():
    running = True
    playing = True
    count = 0
    fps = FPS(BLACK)
    update_freq = 12
    play_music = True

    if play_music:
        audio = "audio/lofi_no_copyright.mp3"
        stream_time = 0
        beats = detect_beats(audio)
        mixer.music.load(audio)
        mixer.music.play()

    positions = set()

    while running:
        fps.clock.tick(120)

        if playing:
            count += 1
        
        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        last_stream_time = stream_time
        stream_time = round(pygame.mixer.music.get_pos() / 1000, 2)
        print(stream_time)
        if stream_time > last_stream_time and stream_time in beats:
            start_position = (random.randint(0, GRID_WIDTH), random.randint(0, GRID_HEIGHT))
            obj = SpawnObject(start_position, GREEN).matrix_table()
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
                    playing = False
                    count = 0

                ### start own code ###
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

                if event.key == pygame.K_t:
                    positions.add((2,1, GREEN))
                ### end own code ###
         
        screen.fill(GREY)
        draw_grid(positions)
        fps.render(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

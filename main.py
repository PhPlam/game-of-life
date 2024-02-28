import pygame
import random
import numpy as np
from spawnobject import SpawnObject, FPS
import sys

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
DARKER_GREY = (120, 120, 120)
YELLOW = (255, 255, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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

def main():
    running = True
    playing = False
    count = 0
    fps = FPS(BLACK)
    update_freq = 12

    positions = set()
    while running:
        fps.clock.tick(60)
        
        if playing:
            count += 1
        
        if count >= update_freq:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row, RED)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                ### start own code ###
                if event.key == pygame.K_s:
                    glider = SpawnObject(GRID_WIDTH, GRID_HEIGHT, BLUE).matrix_glider()
                    for position in glider:
                        positions.add(position)

                if event.key == pygame.K_a:
                    pento = SpawnObject(GRID_WIDTH, GRID_HEIGHT, GREEN).matrix_rpentomino()
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

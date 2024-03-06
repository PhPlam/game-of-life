# date: 06. march 2024

import numpy as np
import random
import pygame


class SpawnObject:

    def __init__(self, start_position, color):
        self.start_pos = start_position
        self.color = color

    def matrix_glider(self):
        # glider
        # 0|1|0
        # 0|0|1
        # 1|1|1
        object_matrix = np.array([[0,1,0],
                                  [0,0,1],
                                  [1,1,1]]).T

        object_matrix = np.rot90(object_matrix, random.randint(0,3))
        positions_on_grid = self.set_positions(object_matrix)
        return positions_on_grid

    def matrix_rpentomino(self):
        # R-Pentomino
        # 0|1|1
        # 1|1|0
        # 0|1|0

        object_matrix = np.array([[0,1,1],
                                  [1,1,0],
                                  [0,1,0]]).T
 
        object_matrix = np.rot90(object_matrix, random.randint(0,3))
        positions_on_grid = self.set_positions(object_matrix)
        return positions_on_grid

    def matrix_table(self):
        # Table
        # 1|1|1|1
        # 1|0|0|1

        object_matrix = np.array([[1, 1, 1, 1],
                                  [1, 0, 0, 1]]).T

        object_matrix = np.rot90(object_matrix, random.randint(0, 3))
        positions_on_grid = self.set_positions(object_matrix)
        return positions_on_grid

    def set_positions(self, object_matrix):       
        positions_set = set()
        for i in range(np.shape(object_matrix)[0]):
            for j in range(np.shape(object_matrix)[1]):
                if object_matrix[i][j]:
                    positions_set.add((self.start_pos[0]+i, self.start_pos[1]+j, self.color))          
        return positions_set


class FPS:
    def __init__(self, color):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, color)
        self.color = color
 
    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(),2)), True, self.color)
        display.blit(self.text, (10, 10))
import sys
import numpy as np

import pygame

from settings import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')

        self.screen.fill(BLACK)

        self.board = np.zeros((ROWS, COLS))
        self.draw_lines()
        self.draw_board()

    def draw_lines(self, color = WHITE):
        for i in range(1, ROWS):
            pygame.draw.line(self.screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            pygame.draw.line(self.screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1: # Draw O(player) 
                    pygame.draw.circle(self.screen, WHITE, ((SQUARE_SIZE // 2) + (col * SQUARE_SIZE), (SQUARE_SIZE // 2) + (row * SQUARE_SIZE)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                
                elif self.board[row][col] == 2: # Draw X(agent)
                    pygame.draw.line(self.screen, WHITE, ((SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), ((3*SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (3*SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), LINE_WIDTH)
                    pygame.draw.line(self.screen, WHITE, ((3*SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), ((SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (3*SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), LINE_WIDTH)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
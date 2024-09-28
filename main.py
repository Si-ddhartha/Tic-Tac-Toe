import sys
import numpy as np

import pygame

from minimax import AI

from settings import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')

        icon = pygame.image.load('icon.png').convert_alpha()
        pygame.display.set_icon(icon)

        self.initialize_game()

        self.ai = AI(self)

    def initialize_game(self):
        self.board = np.zeros((ROWS, COLS))
        self.screen.fill(BLACK)

        self.draw_lines()
        self.draw_board()

        self.player_turn = True
        self.game_over = False

    def draw_lines(self, color = WHITE):
        for i in range(1, ROWS):
            pygame.draw.line(self.screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            pygame.draw.line(self.screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

    def draw_board(self, color = WHITE):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1: # Draw O(player) 
                    pygame.draw.circle(self.screen, color, ((SQUARE_SIZE // 2) + (col * SQUARE_SIZE), (SQUARE_SIZE // 2) + (row * SQUARE_SIZE)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                
                elif self.board[row][col] == 2: # Draw X(AI)
                    pygame.draw.line(self.screen, color, ((SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), ((3*SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (3*SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), CROSS_WIDTH)
                    pygame.draw.line(self.screen, color, ((3*SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), ((SQUARE_SIZE // 4) + (col * SQUARE_SIZE), (3*SQUARE_SIZE // 4) + (row * SQUARE_SIZE)), CROSS_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def is_square_available(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self, board):
        return np.count_nonzero(board == 0) == 0

    def check_win(self, player, board):
        # Horizontal
        for row in range(ROWS):
            if np.all(board[row, :] == player):
                return True
        
        # Vertical
        for col in range(COLS):
            if np.all(board[:, col] == player):
                return True
        
        # Positive diagonal
        if np.all(np.diag(board) == player):
            return True
        
        # Negative diagonal
        if np.all(np.diag(np.fliplr(board)) == player):
            return True
        
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit()

                if self.game_over:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r: # Press 'r' to restart game
                        self.initialize_game()
                
                else:
                    if self.player_turn:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseX = event.pos[0]
                            mouseY = event.pos[1]

                            clicked_row = mouseY // SQUARE_SIZE
                            clicked_col = mouseX // SQUARE_SIZE

                            if self.is_square_available(clicked_row, clicked_col):
                                self.mark_square(clicked_row, clicked_col, 1)
                                if self.check_win(1, self.board):
                                    self.game_over = True

                                self.player_turn = False
                
                    else:
                        if not self.game_over:
                            row, col = self.ai.best_move()
                            if row is not None and col is not None:
                                self.mark_square(row, col, 2)
                                if self.check_win(2, self.board):
                                    self.game_over = True

                            self.player_turn = True

            if self.is_board_full(self.board) and not self.game_over:
                self.game_over = True

            if self.game_over:
                if self.check_win(1, self.board):
                    self.draw_lines(GREEN)
                    self.draw_board(GREEN)

                elif self.check_win(2, self.board):
                    self.draw_lines(RED)
                    self.draw_board(RED)
                
                else:
                    self.draw_lines(GRAY)
                    self.draw_board(GRAY)
            
            else:
                self.draw_board()
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
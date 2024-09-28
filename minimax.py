import numpy as np

from settings import *

class AI:

    def __init__(self, game):
        self.game = game
        self.max_depth = 9

    def is_terminal_state(self, board):
        # Check for terminal states
        if self.game.check_win(2, board): # AI wins
            return (True, np.inf)

        if self.game.check_win(1, board): # Player wins
            return (True, -np.inf)

        if self.game.is_board_full(board): # Draw
            return (True, 0)

        return (False, 0)

    def minimax(self, board, depth, maximizing_player):
        is_terminal, score = self.is_terminal_state(board)

        if is_terminal or depth == self.max_depth:
            return score

        if maximizing_player:
            best_score = -np.inf
            for row in range(ROWS):
                for col in range(COLS):
                    if self.game.is_square_available(row, col):
                        board[row][col] = 2
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = 0

                        best_score = max(best_score, score)
            
            return best_score
        
        else:
            best_score = np.inf
            for row in range(ROWS):
                for col in range(COLS):
                    if self.game.is_square_available(row, col):
                        board[row][col] = 1
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = 0

                        best_score = min(best_score, score)

            return best_score

    def best_move(self):
        best_score = -np.inf
        move = None

        for row in range(ROWS):
            for col in range(COLS):
                if self.game.is_square_available(row, col):
                    self.game.board[row][col] = 2
                    score = self.minimax(self.game.board, 0, False)
                    self.game.board[row][col] = 0

                    if score > best_score:
                        best_score = score
                        move = (row, col)

        return move

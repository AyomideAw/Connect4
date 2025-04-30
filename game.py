import numpy as np

ROWS, COLS = 6, 7

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.current_player = 1
        return self.get_state()

    def drop_piece(self, col):
        if not self.is_valid_move(col):
            return False
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                break
        return True

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def is_valid_move(self, col):
        return self.board[0][col] == 0

    def get_valid_moves(self):
        return [col for col in range(COLS) if self.is_valid_move(col)]

    def is_terminal(self):
        return self.check_winner() != 0 or len(self.get_valid_moves()) == 0

    def check_winner(self):
        for c in range(COLS - 3):
            for r in range(ROWS):
                if self.same(self.board[r][c:c+4]):
                    return self.board[r][c]

        for c in range(COLS):
            for r in range(ROWS - 3):
                if self.same(self.board[r:r+4, c]):
                    return self.board[r][c]

        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if self.same([self.board[r+i][c+i] for i in range(4)]):
                    return self.board[r][c]

        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if self.same([self.board[r-i][c+i] for i in range(4)]):
                    return self.board[r][c]

        return 0

    def same(self, line):
        return len(set(line)) == 1 and line[0] != 0

    def get_state(self):
        return tuple(map(tuple, self.board))  # hashable for Q-table

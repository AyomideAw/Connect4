from game import ConnectFour
import numpy as np

class ConnectFourEnv:
    def __init__(self):
        self.game = ConnectFour()

    def reset(self):
        return self.game.reset()

    def step(self, action):
        valid = self.game.drop_piece(action)
        if not valid:
            return self.game.get_state(), -10, True

        winner = self.game.check_winner()
        done = self.game.is_terminal()

        reward = 1 if winner == self.game.current_player else 0
        next_state = self.game.get_state()
        self.game.switch_player()
        return next_state, reward, done

    def get_valid_actions(self):
        return self.game.get_valid_moves()

    def get_flat_state(self):
        return np.array(self.game.board).flatten()

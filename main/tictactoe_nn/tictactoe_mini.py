import numpy as np
import pysnooper

class TicTacToeState_Mini(object):
    def __init__(self, board):
        self.board = board.copy()
    def __str__(self):
        return "\n".join(["".join(row) for row in self.board])
    def is_leaf(self):
        if self.score_for_max_player() != 0: return True
        return (self.board == "_").sum() == 0
    def score_for_max_player(self):
        # max player is X
        for player, score in zip("XO", [+1, -1]):
            if (self.board == player).all(axis=0).any(): return score
            if (self.board == player).all(axis=1).any(): return score
            if (np.diag(self.board) == player).all(): return score
            if (np.diag(np.rot90(self.board)) == player).all(): return score
        return 0
    def is_max_players_turn(self):
        return (self.board == "O").sum() == (self.board == "X").sum()
    def is_min_players_turn(self):
        return not self.is_max_players_turn()
    def valid_actions(self):
        return list(zip(*np.nonzero(self.board == "_")))
    def perform(self, action):
        player = "X" if self.is_max_players_turn() else "O"
        row, col = action
        new_state = TicTacToeState(self.board)
        new_state.board[row, col] = player
        return new_state

def initial_mini_state(board=None):
    if board is None:
        board = np.empty((3,3), dtype=str)
        board[:] = "_"
    return TicTacToeState_Mini(board)

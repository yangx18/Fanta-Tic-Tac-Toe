import numpy as np
import pysnooper
from tictactoe_mini import initial_mini_state

class TicTacToeState(object):
    def __init__(self, board, action):
        self.board = board.copy()
        self.last_action = action

    def is_max_players_turn(self,boolean=1):
        return (self.board == "O").sum() == (self.board == "X").sum()
    def is_min_players_turn(self):
        return not self.is_max_players_turn()
    def valid_actions(self):
        actions = list(zip(*np.nonzero(self.board == "_")))
        true_valid = []

        for action in actions:
            if self.last_action == (action[0],action[1]):
                temp_state = initial_mini_state(self.board[action[0],action[1]])
                if temp_state.is_leaf():
                    continue
                else:
                    true_valid.append(action)
        #random pick if defined grid unavliable
        if true_valid == []:
            for action in actions:
                if self.last_action != (action[0],action[1]):
                    temp_state = initial_mini_state(self.board[action[0],action[1]])
                    if temp_state.is_leaf():
                        continue
                    else:
                        true_valid.append(action)

        return true_valid

    def is_leaf_leaf(self):
        if self.score_for_max_max_player()!=0:return True
        if self.valid_actions() == []: return True
        return (self.board == "_").sum() == 0
    #@pysnooper.snoop(depth=1)
    def score_for_max_max_player(self):
        for player, score in zip("XO",[+1,-1]):
            #Rows
            state = []
            for i in range(3):
                state.append([initial_mini_state(self.board[i][0]), initial_mini_state(self.board[i][1]), initial_mini_state(self.board[i][2])])
                if (state[i][0].is_leaf() and state[i][1].is_leaf()
                    and state[i][2].is_leaf()):

                    if (state[i][0].score_for_max_player() == state[i][1].score_for_max_player()
                        == state[i][2].score_for_max_player()):

                        return state[i][0].score_for_max_player()
            #Cols
            for j in range(3):
                if (state[0][j].is_leaf() and state[1][j].is_leaf()
                    and state[2][j].is_leaf()):

                     if (state[0][j].score_for_max_player() == state[1][j].score_for_max_player()
                        == state[2][j].score_for_max_player()):

                         return state[0][j].score_for_max_player()

            #Diag x

            if (state[0][0].is_leaf() and state[1][1].is_leaf()
                and state[2][2].is_leaf()):

                if (state[0][0].score_for_max_player() == state[1][1].score_for_max_player()
                    == state[2][2].score_for_max_player()):

                    return state[1][1].score_for_max_player()
            #Diag y
            if (state[0][2].is_leaf() and state[1][1].is_leaf()
                and state[2][0].is_leaf()):

                if (state[0][2].score_for_max_player() == state[1][1].score_for_max_player()
                    == state[2][0].score_for_max_player()):

                    return state[1][1].score_for_max_player()
        #Tie
        return 0

    def perform_extra(self, action):
        player = "X" if self.is_max_players_turn() else "O"
        row_out, col_out, row_in, col_in = action
        new_state = TicTacToeState(self.board, (row_in, col_in))
        new_state.board[row_out, col_out, row_in, col_in] = player
        return new_state


    def print_func(self):
        for i in range(3):
            print('{0} | {1} | {2}\n'.format(self.board[0][0][i],self.board[0][1][i],self.board[0][2][i]))
        print('--------------------------------------------')
        for i in range(3):
            print('{0} | {1} | {2}\n'.format(self.board[1][0][i],self.board[1][1][i],self.board[1][2][i]))
        print('--------------------------------------------')
        for i in range(3):
            print('{0} | {1} | {2}\n'.format(self.board[2][0][i],self.board[2][1][i],self.board[2][2][i]))
        print('--------------------------------------------')


def initial_state(obstacles=0):
    board =  np.array([
  [[["_" for _ in range(3)] for _ in range(3)]
     for large_column in range(3)]
      for large_row in range(3)])

    for i in range(obstacles):
        obs = np.random.randint(3, size=4)
        board[obs[0],obs[1],obs[2],obs[3]] = 'P'

    return TicTacToeState(board,(0,0))


if __name__ == "__main__":
    state = initial_state()
    print(state.print_func())
    print(state.valid_actions())

    while True:
        if state.is_leaf_leaf(): break
        actions = state.valid_actions()

        print('available actions:\n',actions)
        if len(actions) == 0: break

        state = state.perform_extra(actions[0])
        print(state.print_func())

    print("max score, is over:")
    if (state.score_for_max_max_player() == 1):
        print('X wins')
    elif (state.score_for_max_max_player() == -1):
        print("O wins")
    else: print('Tie')

    print(state.is_leaf_leaf())

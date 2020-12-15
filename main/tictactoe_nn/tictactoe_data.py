import itertools as it
import mcts as mcts
import tictactoe as ttt
import torch as tr
import numpy as np
import pysnooper

def generate(num_games=25, num_rollouts=50, choose_method=None):


    if choose_method is None:
        choose_method = mcts.puct

    data = []
    for game in range(num_games):

        state = ttt.initial_state()
        for turn in it.count():
            print("game %d, turn %d..." % (game, turn))

            # Stop when game is over
            if state.is_leaf_leaf(): break

            # Act immediately if only one action available
            valid_actions = state.valid_actions()
            if len(valid_actions) == 1:
                state = state.perform_extra(valid_actions[0])
                continue

            # Otherwise, use MCTS
            node, a = mcts.mcts(state, num_rollouts, choose_method=choose_method)
            state = node.children()[a][0].state

            # Add child states and their values to the data
            Q = node.get_score_estimates()
            for c, (child,_) in enumerate(node.children()):
                data.append((child.state, Q[c]))

    return data

def encode(state):

    s = tr.zeros(9,3,3,3)
    i = 0
    for row_out in range(3):
        for col_out in range(3):
            for row in range(3):
                for col in range(3):
                    if state.board[row_out,col_out,row,col] =='_':
                        s[i,0,row,col] = 1
                    if state.board[row_out,col_out,row,col] =='O':
                        s[i,1,row,col] = 1
                    if state.board[row_out,col_out,row,col] =="X":
                        s[i,2,row,col] = 1
            i += 1
    return s

#@pysnooper.snoop(watch=('output'),depth=1)
def get_batch( num_games=50, num_rollouts=50, choose_method =None):
    data_gen = generate(num_games,num_rollouts, choose_method)
    arr = []
    arr_score = []
    for (s,v) in data_gen:
        print(s,v)
        arr.append(encode(s))
        arr_score.append(v)

    actual_s = tr.stack(arr)
    score_s = tr.tensor([arr_score],dtype=tr.float32).t()
    #score_st = tr.reshape(score_s,(len(arr_score),1))
    return (actual_s,score_s)


if __name__ == "__main__":
    board_size = 9
    instance_size = int(input('instance size/the number of obstacles(0-4) 5 different size:\n'))
    num_games = 50
    num_rollouts = 50
    inputs, outputs = get_batch(num_games=num_games,num_rollouts=num_rollouts,choose_method=mcts.puct)
    print(inputs[-1])
    print(outputs[-1])

    import pickle as pk
    with open("data%d.pkl" % instance_size, "wb") as f: pk.dump((inputs, outputs), f)

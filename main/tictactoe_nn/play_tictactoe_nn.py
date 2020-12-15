import itertools as it
import random
import numpy as np
import torch as tr
import tictactoe as tt
import mcts as mcts
import tictactoe_data as td
import tictactoe_net as tn
from tictactoe_mini import initial_mini_state
import matplotlib.pyplot as plt
import pysnooper

#@pysnooper.snoop(depth=1)
def nn_puct(node):
    with tr.no_grad():
        x = tr.stack(tuple(map(td.encode, [child.state for child, _ in node.children()])))
        y = net(x)
        probs = tr.softmax(y.flatten(), dim=0)
        a = np.random.choice(len(probs), p=probs.detach().numpy())
    return node.children()[a][0]

if __name__ == "__main__":

    board_size = 9
    count_ai,count_player = 0,0
    score_ais,score_players = [],[]

    b_size = int(input('Please input the board_size, which in our Tictactoe game represent the obstacles in the board mark as P:(0-4) \n'))
    game_times = int(input('Please input the number of games:\n'))

    net = tn.TictactoeNet(board_size)
    net.load_state_dict(tr.load("model%d.pth" % b_size))

    #Reapet games_times times number of games
    for game_time in range(game_times):
        print(game_time)
        score_ai,score_player = 0,0
        state = tt.initial_state(b_size)
        for step in it.count():
            print(state.print_func())
            print("Step %d" % step)

            # Stop when game is over
            if state.is_leaf_leaf(): break

            # Act immediately if only one action available
            valid_actions = state.valid_actions()
            if len(valid_actions) == 1:
                state = state.perform_extra(valid_actions[0])
                continue

            # Otherwise, if it is the NN AI's turn (max), run NN_MCTS to decide its action
            if  state.is_max_players_turn():
                node, a = mcts.mcts(state,
                    num_rollouts=50, max_depth=25, choose_method=nn_puct)
                state = node.children()[a][0].state
                continue

            #MCTS AI
            if  not state.is_max_players_turn():
                node, a = mcts.mcts(state,max_depth=25,
                    num_rollouts=50, choose_method=mcts.puct)
                state = node.children()[a][0].state
                continue

            '''
            # Otherwise, get next move from user
            while True: # repeat until user chooses a valid action

                action = mcts.input_fun(node.children()[a][1])
                row_out,col_out,row_in,col_in = action[0],action[1],action[2],action[3]

                vaild_actions = state.valid_actions()
                if (row_out,col_out,row_in,col_in) not in vaild_actions:
                    print('please reinput correct row and col\n')
                    continue

                # action was valid, exit the busy loop
                break
             '''
            # perform selected action
            state = state.perform_extra(action)

        print("Game over!\n================================")
        #caculate score
        for i in range(3):
            for j in range(3):
                state_temp = initial_mini_state(state.board[i,j])
                if state_temp.score_for_max_player()>0: score_ai += 1
                elif state_temp.score_for_max_player()<0: score_player +=1

        score_ai_total = score_ai-score_player
        score_player_total = score_player-score_ai
        #caculate the wining times
        if state.score_for_max_max_player()>0:
            print("NN_AI wins")
            count_ai += 1
            #if nn-ai wins but loss the score, we say it wins 0 score
            if score_ai_total<0:
                score_ai_total = 0
        elif state.score_for_max_max_player()==0:
            print('tie')
        else:
            print("player wins")
            count_player += 1
            #if player wins but loss the score, we say it wins 0 score
            if score_player_total < 0:
                score_player_total = 0


        score_ais.append(score_ai_total)
        score_players.append(score_player_total)

    print('Instance size '+str(b_size))
    print('Win games for ai-nn: {0} times\nWin games for mcts-ai: {1} times'.format(count_ai,count_player))
    print('total score of AI-nn',sum(score_ais))
    print("total score of AI-mctstree",sum(score_players))

    print('score for ai with NN in each play: {0}\nscore for mcts-ai in each play: {1}'.format(score_ais,score_players))

    #Plot Histogram
    x = score_ais
    hist, bins = np.histogram(x, bins=[i for i in range(-5,6)])
    plt.hist(x, bins, histtype='bar', edgecolor="black", align='mid',rwidth=0.9)
    plt.xlabel('Score of NN_MCTS_AI')
    plt.ylabel('Count')

    title = 'NN_Mcts_AI---Instance Size '+str(b_size)
    plt.title(title)
    plt.show()

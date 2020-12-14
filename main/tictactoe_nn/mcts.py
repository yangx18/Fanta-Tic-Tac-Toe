import numpy as np
import pysnooper
from tictactoe import initial_state
import sys
import random


def puct(node):

    '''
    c = np.argmax([
            p
        for p in puct_probs(node)
        ])
    '''
    #print(puct_probs(node))
    c = np.random.choice(len(node.children()), p=puct_probs(node))
    #print('2:\n')
    #print(c)
    return node.children()[c][0]

def puct_probs(node):
    nc = node.get_visit_counts()
    qc = node.get_score_estimates()
    #UCT
    uc = np.sqrt( (np.log(node.visit_count + 1)) / (nc + 1) ) + qc
    '''
    #Tanh
    uc_n = (np.exp(2*uc)+1)/(np.exp(2*uc)+1)
    '''
    #softmax
    uc_e = np.exp(uc)
    uc_n = uc_e/(uc_e.sum())

    return uc_n

class Node(object):
    def __init__(self, state, depth = 0, choose_method=puct):
        self.state = state
        self.depth = depth
        self.visit_count = 0
        self.score_total = 0
        self.score_estimate = 0
        self.child_list = None # saving (state,cur_action)
        self.choose_method = choose_method
    def children(self):
        if self.child_list is None:
            actions = self.state.valid_actions()
            self.child_list = []
            for action in actions:
                new_state = self.state.perform_extra(action)
                node_child = Node(new_state)
                node_child.depth = self.depth + 1
                self.child_list.append((node_child, action))

        return self.child_list
    #@pysnooper.snoop(depth=1)
    def choose_child(self):
        return self.choose_method(self)

    def get_visit_counts(self):
        visit_count_arr = []
        for child, _ in self.children():
            visit_count_arr.append(child.visit_count)
        return np.array(visit_count_arr)

    #@pysnooper.snoop(depth=1)
    def get_score_estimates(self):
        arr = []
        for child, _ in self.children():
            if child.visit_count == 0:
                 arr.append(0)
            elif self.state.is_max_players_turn():
                arr.append(child.score_estimate)
            else: arr.append(-1*child.score_estimate)
        return np.array(arr)

#@pysnooper.snoop(depth=1)
def rollout(node, max_depth=None):

    if node.depth == max_depth or node.state.is_leaf_leaf():
        result = node.state.score_for_max_max_player()
    else:
        result = rollout(node.choose_child(), max_depth)
        #print(node.state)
    node.visit_count += 1
    node.score_total += result
    node.score_estimate = node.score_total / node.visit_count
    return result

#@pysnooper.snoop(watch=('a'),depth=2)
def mcts(state, num_rollouts, max_depth=100, choose_method=puct):
    node = Node(state, choose_method=choose_method)
    for rollout_counter in range(num_rollouts): rollout(node, max_depth=max_depth)
    for child, state in node.children():
        print(child.score_estimate)
        print(state)

    a = np.argmax([
        child.score_estimate
        for child, _ in node.children()
        ])

    return node, a



def input_fun(last_action,state):
    try:
        a = int(input('x_out'))
        b = int(input('y_out'))
        c = int(input('x_in'))
        d = int(input('y_in'))
    except:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)
        print("Please write correct rows'/cols : \n")
        a,b,c,d = input_fun(last_action,states)

    '''
    for i in state.valid_actions():
        if (last_action[2],last_action[3]) == (i[0],i[1]):
            if (a,b) != (last_action[2],last_action[3]) or
                c >2 or d > 2 or c<0 or d<0:
                print("Please write correct rows'/cols : ",(last_action[2],last_action[3]))
                input_fun(last_action,state)
        elif  c >2 or d > 2 or c<0 or d<0:
            print("Please write correct rows'/cols : randomly")
            input_fun(last_action,state)
    '''
    return(a, b, c, d)




if __name__ == "__main__":

    state = initial_state(obstacles=0)
    print(state.print_func())
    game_type = int(input('1. AI to random OR\n 2.AI to player:\n'))

    ai = 0
    player = 0
    if game_type ==1:
        games_num = int(input('number of games:\n'))
        for i in range(games_num):

            while state.valid_actions()!=[]:
                node, a = mcts(state,50)
                state = node.children()[a][0].state
                print('\n')
                print(state.print_func())

                #player turn
                actions = state.valid_actions()
                if actions == []:break
                random.randint(0,len(actions)-1)
                action = actions[0]

                #action = input_fun(node.children()[a][1])
                state = state.perform_extra(action)

                print("\n")
                print(state.print_func())
            if state.score_for_max_max_player() == 1:
                print('ai win')
                ai += 1
            elif state.score_for_max_max_player() == -1:
                print('player wins')
                player += 1
            else:print('tie')
        print("Ai wins {0} times, random robot wins {1} times".format(ai,player))

    #User player
    elif game_type ==2:
        while state.valid_actions()!=[]:
            node, a = mcts(state,50)
            state = node.children()[a][0].state
            print('\n')
            print(state.print_func())

            #player turn
            action = input_fun(node.children()[a][1],state)
            state = state.perform_extra(action)

            print("\n")
            print(state.print_func())
        if state.score_for_max_max_player() == 1:
            print('ai win')
            ai += 1
        elif state.score_for_max_max_player() == -1:
            print('player wins')
            player += 1
        else:print('tie')

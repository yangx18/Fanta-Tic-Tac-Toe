import numpy as np
import math
import random

def ai_turn(state):

    max_score = -math.inf
    best_action = (-1,-1)

    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                state[i][j] = "O"
                value = minimax(state,False,-math.inf,math.inf)
                state[i][j] = "_"
                if value > max_score:
                    max_score = value
                    best_action = (i,j)

    state[best_action[0]][best_action[1]] = "O"
    print(state)


def game_over(state):
    for symbol in "XO":
        if(state == symbol).all(axis=0).any() : return (True,symbol)
        if(state == symbol).all(axis=1).any() : return (True,symbol)
        if np.diag(state == symbol).all() : return (True,symbol)
        if np.diag(np.rot90(state) == symbol).all() : return (True,symbol)
    if not (state =="_").any():return (True,symbol)
    return (False,symbol)


def score(state):
    for (symbol, sign) in zip("XO",[-1,+1]):
        if(state == symbol).all(axis=0).any() : return sign
        if(state == symbol).all(axis=1).any() : return sign
        if np.diag(state == symbol).all() : return sign
        if np.diag(np.rot90(state == symbol)).all() : return sign
    return 0

def minimax(state,max_turn,alpha,beta):

    if game_over(state)[0]:
        return score(state)

    if max_turn:
        max_score = -math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "O"
                    value = minimax(state,False,alpha,beta)
                    state[i][j] = "_"
                    max_score = max(value,max_score)
                    alpha = max(max_score,alpha)
                    if beta >= alpha:
                        break

        return max_score

    else:
        min_score = math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "X"
                    value = minimax(state,True,alpha,beta)
                    state[i][j] = "_"
                    min_score = min(value,min_score)
                    beta = min(min_score,beta)
                    if alpha >= beta:
                        break

        return min_score


if __name__ == "__main__":

    state = np.array([
    ["_" for c in range(3)]
    for r in range(3)
    ])
#ai O , player X
    ai_turn(state)
    cur_turn = "ai"

    while (state =="_").any() and not game_over(state)[0]:

        choicex =input('choice you next action in row:\n')
        choicex = int(choicex)
        while choicex < 0 or choicex > 2:
            choicex =input('choice you next action in row in [0,3]:\n')
            choicex = int(choicex)

        choicey =input('choice you next action in col:\n')
        choicey = int(choicey)
        while choicey <0 or choicex >2:
            choicey =input('choice you next action in col in [0,3]:\n')
            choicey = int(choicey)


        if state[choicex][choicey] =="_":
            state[choicex][choicey] = "X"
            cur_turn = "player"
            print(state)
        else:
            print("ocupied, retry")
            continue

        if (state =="_").any():
            ai_turn(state)
            cur_turn = "ai"
        else:
            break

    print(state)
    if score(state)==0:print("tie!")
    elif game_over(state)[1] == "O":
        print("ai wins this game!")
    else:print("player wins!!!!")

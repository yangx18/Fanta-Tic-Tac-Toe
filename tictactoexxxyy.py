import numpy as np
import math
import random


def game_over(state):
    for symbol in "XO":
        if(state == symbol).all(axis=0).any() :
            return (True,symbol)
        if(state == symbol).all(axis=1).any() :
            return (True,symbol)
        if np.diag(state == symbol).all() :
            return (True,symbol)
        if np.diag(np.rot90(state) == symbol).all() :
            return (True,symbol)

    if not (state =="_").any():return (True,symbol)
    return (False,symbol)

def game_over_out(state):

        #ROW
        for i in range(3):
            a =  (state[i]=='O').all(axis=1)
            b = (state[i]=='O').all(axis=2)
            if (not (a==False).any()) and (not (b==False).any()):
                print('hahaha1')
                return True
        for i in range(3):
            a =  (state[i]=='X').all(axis=1)
            b = (state[i]=='X').all(axis=2)
            if (not (a==False).any()) and (not (b==False).any()):

                return True

        #COL
        a=(state=='X').all(axis=3)
        b = (a ==True).all(axis=2)
        if (b==True).all(axis=0).any():

            return True

        a=(state=='O').all(axis=3)
        b = (a ==True).all(axis=2)
        if (b==True).all(axis=0).any():

            return True

        #DIAG
        if (not (state[0][0] != state[1][1]).any()) and  (not (state[1][1] != state[2][2]).any()):
            if(state[0][0][0][0] != '_'):

                return True

        if (not (state[0][2] != state[1][1]).any()) and  (not (state[1][1] != state[2][0]).any()):
            if(state[0][2][0][0] != '_'):

                return True

        #TIE
        if not (state=="_").any(): return True

        return False



def score(state):
    for (symbol, sign) in zip("XO",[-1,+1]):
        if(state == symbol).all(axis=0).any() : return sign
        if(state == symbol).all(axis=1).any() : return sign
        if np.diag(state == symbol).all() : return sign
        if np.diag(np.rot90(state == symbol)).all() : return sign
    return 0



def ai_turn(state,c,d):

    max_score = -math.inf
    best_action = (-1,-1)

    for i in range(3):
        for j in range(3):
            if state[c][d][i][j] == "_":
                state[c][d][i][j] = "O"
                print('===================')
                value = minimax(state,i,j,False,-math.inf,math.inf,0)
                state[c][d][i][j] = "_"
                if value > max_score:
                    max_score = value
                    best_action = (i,j)

    state[c][d][best_action[0]][best_action[1]] = "O"
    print(state)


def minimax(state,c,d,max_turn,alpha,beta,depth):
    if game_over_out(state):
        return score(state[c][d])
    if game_over(state[c][d])[0]:
        #state[c][d] = game_over(state[c][d])[1]
        return score(state[c][d])

    if max_turn:
        max_score = -math.inf
        for i in range(3):
            for j in range(3):
                if state[c][d][i][j] == "_":
                    state[c][d][i][j] = "O"
                    value = minimax(state,i,j,False,alpha,beta,depth+1)
                    state[c][d][i][j] = "_"
                    max_score = max(value,max_score)
                    alpha = max(max_score,alpha)
                    if beta >= alpha:
                        break

        return max_score

    else:

        min_score = math.inf
        for i in range(3):
            for j in range(3):
                if state[c][d][i][j] == "_":
                    state[c][d][i][j] = "X"
                    value = minimax(state,i,j,True,alpha,beta,depth+1)
                    state[c][d][i][j] = "_"
                    min_score = min(value,min_score)
                    beta = min(min_score,beta)
                    if alpha >= beta:
                        break

        return min_score


if __name__ == "__main__":


    state =  np.array([
      [[["_" for _ in range(3)] for _ in range(3)]
         for large_column in range(3)]
          for large_row in range(3)])


    #ai O , player X
    #AI Turn
    state[0][0][0][0] = "O"
    cur_turn = "ai"
    print(state)

    while (state =="_").any() and  not game_over_out(state):

        a = input("a:\n:")
        b = input("b:\n:")
        c = input("c:\n:")
        d = input("d:\n:")
        a,b,c,d = int(a),int(b),int(c),int(d)

        if state[a][b][c][d] == "_":
            state[a][b][c][d] = "X"
            if game_over(state[a][b])[0]:
                state[a][b] ="X"
            cur_turn = "player"
            print(state)
        else:
            print("ocupied, retry")
            continue


        if (state[c][d] =="_").any() :
            ai_turn(state,c,d)
            if game_over(state[c][d])[0]:
                state[a][b] ="O"
            cur_turn = "ai"
        else:
            for i in range(3):
                for j in range(3):
                    if (state[i][j] =="_").any():
                        ai_turn(state,i,j)
                        if game_over(state[i][j])[0]:
                            state[a][b] ="O"
                        cur_turn = "ai"

        print( (state =="_").any())
        print( game_over_out(state))
        print(state)

    print(state)

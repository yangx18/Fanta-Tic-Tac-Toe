import numpy as np
import random

#Game Over Check For Each same Tic tac toe
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

#Game Over Check For Whole Tic tac toe
def game_over_out(state):

        #ROW
        for i in range(3):
            a =  (state[i]=='O').all(axis=1)
            b = (state[i]=='O').all(axis=2)
            if (not (a==False).any()) and (not (b==False).any()):
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


#return Socre
def score(state):
    for (symbol, sign) in zip("XO",[-1,+1]):
        if(state == symbol).all(axis=0).any() : return sign
        if(state == symbol).all(axis=1).any() : return sign
        if np.diag(state == symbol).all() : return sign
        if np.diag(np.rot90(state == symbol)).all() : return sign
    return 0


#Ai's move action choice
def ai_turn(state):

    max_score = float("-inf")
    best_actionx = -1
    best_actony = -1

    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                state[i][j] = "O"
                value = minimax(state,False,float("-inf"),float("+inf"))
                state[i][j] = "_"
                if value > max_score:
                    max_score = value
                    best_actionx = i
                    best_actiony = j

    state[best_actionx][best_actiony] = "O"

#Minimax Algorithm
def minimax(state,max_turn,alpha,beta):

    if game_over(state)[0]:
        return score(state)

    if max_turn == True:
        max_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "O"
                    value = minimax(state,False,alpha,beta)
                    state[i][j] = "_"
                    max_score = max(value,max_score)
                    alpha = max(max_score,alpha)
                    if max_score >= beta:
                        return max_score


        return max_score

    else:
        min_score = float("inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "X"
                    value = value = minimax(state,True,alpha,beta)
                    state[i][j] = "_"
                    min_score = min(value,min_score)
                    beta = min(min_score,beta)
                    if min_score <= alpha:
                        return min_score


        return min_score


def print_func(state):
    for i in range(3):
        print('{0} | {1} | {2}\n'.format(state[0][0][i],state[0][1][i],state[0][2][i]))
    print('--------------------------------------------')
    for i in range(3):
        print('{0} | {1} | {2}\n'.format(state[1][0][i],state[1][1][i],state[1][2][i]))
    print('--------------------------------------------')
    for i in range(3):
        print('{0} | {1} | {2}\n'.format(state[2][0][i],state[2][1][i],state[2][2][i]))
    print('--------------------------------------------')





if __name__ == "__main__":

    #3x3x3x3 numpy array to represent the Tic-Tac-Toe
    state =  np.array([
      [[["_" for _ in range(3)] for _ in range(3)]
         for large_column in range(3)]
          for large_row in range(3)])


    #Random obstacle
    state[random.randint(0,1)][random.randint(0,2)][random.randint(0,2)][random.randint(0,2)] = 'P'
    state[random.randint(0,2)][random.randint(0,2)][random.randint(0,2)][random.randint(0,2)] = 'P'
    state[random.randint(0,2)][random.randint(0,2)][random.randint(0,2)][random.randint(0,2)] = 'P'

    #Ai is O , player is  X

    #AI Turn
    state[1][1][0][0] = "O"
    cur_turn = "ai"
    print('There are 3 P which represent the obstacle\n')
    print_func(state)

    #Keeping Gamming
    while (state =="_").any() and  not game_over_out(state):

        a,b,c,d=-1,-1,-1,-1
        while (a<0 or a>3) or (b<0 or b>3) or (c<0 or c>3) or (d<0 or d>3):
            print('Please Input correct Int number! bewtween 0-2!\n')

            print('====================================================')
            print('please followe the rule!!!!')
            print('====================================================\n')
            a = input("which row you select in our big tic(0 - 2 rows)?:\n:")
            b = input("which col you select in our big tic(0 - 2 cols)?:\n:")
            c = input("which row you select in small tic(0 - 2 rows)?:\n:")
            d = input("which col you select in small tic?(0 - 2 cols):\n:")
            print("\n")
            try:
                a,b,c,d = int(a),int(b),int(c),int(d)
            except:
                print('Please Input correct number!\n')
                a,b,c,d=-1,-1,-1,-1


        if state[a][b][c][d] == "_":
            state[a][b][c][d] = "X"
            if game_over(state[a][b])[0]:
                state[a][b] ="X"
            cur_turn = "player"

            print('======================Your Move============================\n')
            print_func(state)
            print('\n')

        else:
            print("ocupied, please retry")
            continue

        if game_over_out(state):
            print('================Game Over====================')
            print('Your win!')
            print('=============================================\n')
            break


        if (state[c][d] =="_").any() :
            ai_turn(state[c][d])
            if game_over(state[c][d])[0]:
                state[c][d] ="O"
            cur_turn = "ai"

        else:
            #Find a tic-tac-toe which can win by place only one more move
            for i in range(3):
                for j in range(3):
                    if (state[i][j] == "_").any():
                        state_temp = state.copy()
                        ai_turn(state_temp[i][j])
                        if game_over(state_temp[i][j])[0]:
                            ai_turn(state[i][j])
                            state[i][j] ="O"
                            cur_turn = "ai"
                            break

                else: continue
                break

            #If did not find that move, we random pick one gird
            if cur_turn != "ai":

                ramd_move = (random.randint(0,2),random.randint(0,2))

                if (state[ramd_move[0]][ramd_move[1]] =="_").any():
                    ai_turn(state[ramd_move[0]][ramd_move[1]])
                    if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                        state[ramd_move[0]][ramd_move[1]] ="O"
                    cur_turn = "ai"
                else:

                    for i in range(3):
                        for j in range(3):
                            if (state[i][j] == "_").any():
                                ai_turn(state[i][j])
                                if game_over(state[i][j])[0]:
                                    state[i][j] ="O"
                                cur_turn = "ai"
                                break
                        else: continue
                        break

        if game_over_out(state):
            print('================Game Over====================')
            print('Your Lose!')
            print('=============================================\n')
            break


        #print( (state =="_").any())
        #print( game_over_out(state))
        print('===================Below is Ai\'s move=====================\n')
        print_func(state)
        print('===================Now This is Your Turn====================\n \n')

    # Final Situation
    print_func(state)

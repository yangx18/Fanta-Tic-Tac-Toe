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

#Ai_X's move action choice
def ai_2_turn(state):

    max_score = float("-inf")
    best_action = (0,0)
    nodes_num = 0
    min_depth = -float('inf')


    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                state[i][j] = "X"
                value, nodes_num, depth = minimax_ai2(state,False,float("-inf"),float("+inf"),nodes_num,0)

                unique, counts = np.unique(state,return_counts=True)
                xo_num = dict(zip(unique,counts))

                if 'O' in xo_num and xo_num['O'] >xo_num['X']:
                    state[i][j] = "_"
                    if value >= max_score and depth > min_depth:
                        max_score = value
                        min_depth = depth
                        best_action = (i,j)
                else:
                    state[i][j] = "_"
                    if value > max_score:
                        max_score = value
                        best_action = (i,j)

    state[best_action[0]][best_action[1]] = "X"
    return nodes_num,best_action

#return Socre
def score_ai2(state):
    for (symbol, sign) in zip("OX",[-1,+1]):
        if(state == symbol).all(axis=0).any() : return sign
        if(state == symbol).all(axis=1).any() : return sign
        if np.diag(state == symbol).all() : return sign
        if np.diag(np.rot90(state == symbol)).all() : return sign
    return 0

#Minimax Algorithm
def minimax_ai2(state,max_turn,alpha,beta,nodes_num,depth):

    if game_over(state)[0]:
        nodes_num += 1
        return (score_ai2(state),nodes_num,depth)

    if max_turn == True:
        max_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "X"
                    value, nodes_num, depth = minimax_ai2(state,False,alpha,beta,nodes_num,depth+1)
                    state[i][j] = "_"
                    max_score = max(value,max_score)
                    alpha = max(max_score,alpha)
                    if max_score >= beta:
                        return (max_score, nodes_num, depth)

        return (max_score, nodes_num, depth)

    else:
        min_score = float("inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "O"
                    value, nodes_num, depth  = minimax_ai2(state,True,alpha,beta,nodes_num,depth+1)
                    state[i][j] = "_"
                    min_score = min(value,min_score)
                    beta = min(min_score,beta)
                    if min_score <= alpha:
                        return (min_score, nodes_num, depth)

        return (min_score, nodes_num, depth)

#Ai's move action choice
def ai_1_turn(state):

    max_score = float("-inf")
    best_action = (0,0)
    nodes_num = 0
    min_depth = -float('inf')


    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                state[i][j] = "O"
                value, nodes_num, depth = minimax(state,False ,float("-inf"),float("+inf"),nodes_num,0)

                unique, counts = np.unique(state,return_counts=True)
                xo_num = dict(zip(unique,counts))


                if 'X' in xo_num and xo_num['X'] >xo_num['O']:
                    state[i][j] = "_"
                    if value >= max_score and depth > min_depth:
                        max_score = value
                        min_depth = depth
                        best_action = (i,j)
                else:
                    state[i][j] = "_"
                    if value > max_score:
                        max_score = value
                        best_action = (i,j)

    state[best_action[0]][best_action[1]] = "O"
    return nodes_num,best_action


#Ai's move action choice
def ai_turn(state):

    max_score = float("-inf")
    best_action = (0,0)
    nodes_num = 0
    min_depth = -float('inf')


    for i in range(3):
        for j in range(3):
            if state[i][j] == "_":
                state[i][j] = "O"
                value, nodes_num, depth = minimax(state,False,float("-inf"),float("+inf"),nodes_num,0)

                unique, counts = np.unique(state,return_counts=True)
                xo_num = dict(zip(unique,counts))

                if 'O' not in xo_num:
                    if 'X' in xo_num and (xo_num['X']>1) :
                        state[i][j] = "_"
                        if value >= max_score and depth > min_depth:
                            max_score = value
                            min_depth = depth
                            best_action = (i,j)
                    else:
                        state[i][j] = "_"
                        if value > max_score:
                            max_score = value
                            best_action = (i,j)
                else:
                    if 'X' in xo_num and xo_num['X'] >xo_num['O']:
                        state[i][j] = "_"
                        if value >= max_score and depth > min_depth:
                            max_score = value
                            min_depth = depth
                            best_action = (i,j)
                    else:
                        state[i][j] = "_"
                        if value > max_score:
                            max_score = value
                            best_action = (i,j)

    state[best_action[0]][best_action[1]] = "O"
    return nodes_num

#Minimax Algorithm
def minimax(state,max_turn,alpha,beta,nodes_num,depth):

    if game_over(state)[0]:
        nodes_num += 1
        return (score(state),nodes_num,depth)

    if max_turn == True:
        max_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "O"
                    value, nodes_num, depth = minimax(state,False,alpha,beta,nodes_num,depth+1)
                    state[i][j] = "_"
                    max_score = max(value,max_score)
                    alpha = max(max_score,alpha)
                    if max_score >= beta:
                        return (max_score, nodes_num, depth)


        return (max_score, nodes_num, depth)

    else:
        min_score = float("inf")
        for i in range(3):
            for j in range(3):
                if state[i][j] == "_":
                    state[i][j] = "X"
                    value, nodes_num, depth  = minimax(state,True,alpha,beta,nodes_num,depth+1)
                    state[i][j] = "_"
                    min_score = min(value,min_score)
                    beta = min(min_score,beta)
                    if min_score <= alpha:
                        return (min_score, nodes_num, depth)


        return (min_score, nodes_num, depth)


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
    #@yxiao09

    #3x3x3x3 numpy array to represent the Tic-Tac-Toe
    state =  np.array([
      [[["_" for _ in range(3)] for _ in range(3)]
         for large_column in range(3)]
          for large_row in range(3)])

    #Random obstacle
    obs_nums = input('\nPlease input the number of obstacle you want between 0-4 in int number\n0-non obstacle, 1-one obstacle, 2-two obstacles, 3-three obstacles, 4-four obstacles:')
    obs_nums = int(obs_nums)

    for i in range(obs_nums):
        state[random.randint(0,2)][random.randint(0,2)][random.randint(0,2)][random.randint(0,2)] = 'P'
    print_func(state)


    #Ai is O , player is  X
    choice_ai = input('''plase choose the difficuty of the AI:\n
    1. tree-based one\n
    2."baseline" AI:\n
    3.tree-based ai vs tree based ai:\n
    4.tree-based ai vs baseline ai:\n ''')

    while True:
        try:
            choice_ai = int( choice_ai)
            break
        except:
            choice_ai = input('Plase input a int number bewtween 1 and 4.\n plase choose the difficuty of the AI:\n 1. tree-based one\n \
            2."baseline" AI:\n 3.tree-based ai vs tree based ai:\n4.tree-based ai vs baseline ai\n ')


    if choice_ai == 1:
        print('============================================')
        print('tree-based choosed')
        print('=============================================')
    elif choice_ai == 2:
        print('============================================')
        print('baseline choosed')
        print('=============================================')
    elif choice_ai == 3:
        print('============================================')
        print('tree-based ai vs tree based ai')
        print('=============================================')
    elif choice_ai == 4:
        print('============================================')
        print('tree-based ai vs baseline ai')
        print('=============================================')

    if choice_ai == 3:
        a,b,c,d = (random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2))
        print('ai-1 move')
        state[a][b][c][d] = "O"
        cur_turn = 'ai'
        print_func(state)

    elif choice_ai == 4:
        a,b,c,d = (random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2))
        print('\nbaseline ai(X) move\n')
        state[a][b][c][d] = "X"
        cur_turn = 'player'
        print_func(state)

    else:
        #AI Turn
        state[1][1][0][0] = "O"
        cur_turn = "ai"
        print('There are 3 P which represent the obstacle\n')
        print_func(state)

    #Keeping Gamming
    while (state =="_").any() and  not game_over_out(state):

        if choice_ai == 3 :

            #======================AI-2(X)======================
            print('======================AI-2(X)======================')

            unique, counts = np.unique(state[a][b],return_counts=True)
            xo_num = dict(zip(unique,counts))
            unique_sub, counts_sub = np.unique(state[c][d],return_counts=True)
            xo_num_sub = dict(zip(unique_sub,counts_sub))

            nodes_num = 0
            #AI TURN
            if (state[c][d] =="_").any() :

                if (('O' in xo_num and 'X' in xo_num and xo_num['O'] > xo_num['X']) or
                 ('O' in xo_num and 'X' not in xo_num and xo_num['O']>0)):
                    if '_' in xo_num_sub and xo_num_sub['_'] >1 and state[c][d][a][b] =='_':
                        state[c][d][a][b] = 'P'
                        nodes_num,best_action = ai_2_turn(state[c][d])
                        state[c][d][a][b] ='_'
                    else:
                        nodes_num,best_action = ai_2_turn(state[c][d])
                else:
                    nodes_num,best_action = ai_2_turn(state[c][d])

                if game_over(state[c][d])[0]:
                    state[c][d] =game_over(state[c][d])[1]
                cur_turn = "player"

            else:
                #Find a tic-tac-toe which can win by place only one more move
                for i in range(3):
                    for j in range(3):
                        if (state[i][j] == "_").any():
                            state_temp = state.copy()
                            nodes_num_temp,best_action_temp = ai_2_turn(state_temp[i][j])
                            if game_over(state_temp[i][j])[0]:
                                nodes_num,best_action = ai_2_turn(state[i][j])
                                print("random pick")
                                state[i][j] =game_over(state_temp[i][j])[1]
                                cur_turn = "player"
                                break

                    else: continue
                    break

                #If did not find that move, we random pick one gird
                if cur_turn != "player":

                    ramd_move = (random.randint(0,2),random.randint(0,2))

                    if (state[ramd_move[0]][ramd_move[1]] =="_").any():
                        nodes_num,best_action = ai_2_turn(state[ramd_move[0]][ramd_move[1]])
                        print("random pick")
                        if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                            state[ramd_move[0]][ramd_move[1]] =game_over(state[ramd_move[0]][ramd_move[1]])[1]
                        cur_turn = "player"
                    else:
                        for i in range(3):
                            for j in range(3):
                                if (state[i][j] == "_").any():
                                    nodes_num,best_action = ai_2_turn(state[i][j])
                                    print("random pick")
                                    if game_over(state[i][j])[0]:
                                        state[i][j] =game_over(state[i][j])[1]
                                    cur_turn = "player"
                                    break
                            else: continue
                            break
            print('the number of tree nodes that')
            print('the AI processed before selecting its action: \n', nodes_num)
            print('\n')
            if game_over_out(state):
                print('================Game Over====================')
                print('\nAI-2 Win!\n')
                print('=============================================\n')
                break


            #print( (state =="_").any())
            #print( game_over_out(state))
            print('===================Below is Ai-2\'s move=====================\n')
            print_func(state)
            print('===================Now This is AI-1 Turn====================\n \n')


            a,b,c,d = c,d,best_action[0],best_action[1]


            #=========================ai 1(O)=====================================
            print('======================AI-1(O)=====================')

            unique, counts = np.unique(state[a][b],return_counts=True)
            xo_num = dict(zip(unique,counts))
            unique_sub, counts_sub = np.unique(state[c][d],return_counts=True)
            xo_num_sub = dict(zip(unique_sub,counts_sub))

            nodes_num = 0
            #AI TURN
            if (state[c][d] =="_").any() :

                if (('X' in xo_num and 'O' in xo_num and xo_num['X'] > xo_num['O']) or
                 ('X' in xo_num and 'O' not in xo_num and xo_num['X']>0)):
                    if '_' in xo_num_sub and xo_num_sub['_'] >1 and state[c][d][a][b] =='_':
                        state[c][d][a][b] = 'P'
                        nodes_num,best_action = ai_1_turn(state[c][d])
                        state[c][d][a][b] ='_'
                    else:
                        nodes_num,best_action = ai_1_turn(state[c][d])
                else:
                    nodes_num,best_action = ai_1_turn(state[c][d])

                if game_over(state[c][d])[0]:
                    state[c][d] = game_over(state[c][d])[1]
                cur_turn = "ai"

            else:
                #Find a tic-tac-toe which can win by place only one more move
                for i in range(3):
                    for j in range(3):
                        if (state[i][j] == "_").any():
                            state_temp = state.copy()
                            nodes_num_temp,best_action = ai_1_turn(state_temp[i][j])
                            if game_over(state_temp[i][j])[0]:
                                nodes_num ,best_action= ai_1_turn(state[i][j])
                                print("random pick")
                                state[i][j] =game_over(state_temp[i][j])[1]
                                cur_turn = "ai"
                                break

                    else: continue
                    break

                #If did not find that move, we random pick one gird
                if cur_turn != "ai":
                    print('3')

                    ramd_move = (random.randint(0,2),random.randint(0,2))

                    if (state[ramd_move[0]][ramd_move[1]] =="_").any():
                        nodes_num ,best_action= ai_1_turn(state[ramd_move[0]][ramd_move[1]])
                        print("random pick")
                        if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                            state[ramd_move[0]][ramd_move[1]] ="O"
                        cur_turn = "ai"
                    else:
                        for i in range(3):
                            for j in range(3):
                                if (state[i][j] == "_").any():
                                    nodes_num,best_action = ai_1_turn(state[i][j])
                                    print("random pick")
                                    if game_over(state[i][j])[0]:
                                        state[i][j] =game_over(state[i][j])[1]
                                    cur_turn = "ai"
                                    break
                            else: continue
                            break
            print('the number of tree nodes that')
            print('the AI processed before selecting its action: \n', nodes_num)
            print('\n')
            if game_over_out(state):
                print('================Game Over====================')
                print('\nAI-1 WIN!\n')
                print('=============================================\n')
                break

            print('===================Below is Ai-1\'s move=====================\n')
            print_func(state)
            print('===================Now This is AI-2 Turn====================\n \n')

            a,b,c,d = c,d,best_action[0],best_action[1]

        #==========================================option 4 baseline random AI vs tree based ai======================================================

        elif choice_ai == 4:

            #=========================ai 2(O)=====================================
            print('======================AI-2(O)=====================')

            unique, counts = np.unique(state[a][b],return_counts=True)
            xo_num = dict(zip(unique,counts))
            unique_sub, counts_sub = np.unique(state[c][d],return_counts=True)
            xo_num_sub = dict(zip(unique_sub,counts_sub))

            nodes_num = 0
            #AI TURN
            if (state[c][d] =="_").any() :

                if (('X' in xo_num and 'O' in xo_num and xo_num['X'] > xo_num['O']) or
                 ('X' in xo_num and 'O' not in xo_num and xo_num['X']>0)):
                    if '_' in xo_num_sub and xo_num_sub['_'] >1 and state[c][d][a][b] =='_':
                        state[c][d][a][b] = 'P'
                        nodes_num,best_action = ai_1_turn(state[c][d])
                        state[c][d][a][b] ='_'
                    else:
                        nodes_num,best_action = ai_1_turn(state[c][d])
                else:
                    nodes_num,best_action = ai_1_turn(state[c][d])

                if game_over(state[c][d])[0]:
                    state[c][d] =game_over(state[c][d])[1]
                cur_turn = "ai"

            else:
                #Find a tic-tac-toe which can win by place only one more move
                for i in range(3):
                    for j in range(3):
                        if (state[i][j] == "_").any():
                            state_temp = state.copy()
                            nodes_num_temp,best_action = ai_1_turn(state_temp[i][j])
                            if game_over(state_temp[i][j])[0]:
                                nodes_num ,best_action= ai_1_turn(state[i][j])
                                print("random pick")
                                state[i][j] =game_over(state_temp[i][j])[1]
                                cur_turn = "ai"
                                break

                    else: continue
                    break

                #If did not find that move, we random pick one gird
                if cur_turn != "ai":
                    print('3')

                    ramd_move = (random.randint(0,2),random.randint(0,2))

                    if (state[ramd_move[0]][ramd_move[1]] =="_").any():
                        nodes_num ,best_action= ai_1_turn(state[ramd_move[0]][ramd_move[1]])
                        print("random pick")
                        if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                            state[ramd_move[0]][ramd_move[1]] =game_over(state[ramd_move[0]][ramd_move[1]])[1]
                        cur_turn = "ai"
                    else:
                        for i in range(3):
                            for j in range(3):
                                if (state[i][j] == "_").any():
                                    nodes_num,best_action = ai_1_turn(state[i][j])
                                    print("random pick")
                                    if game_over(state[i][j])[0]:
                                        state[i][j] =game_over(state[i][j])[1]
                                    cur_turn = "ai"
                                    break
                            else: continue
                            break
            print('the number of tree nodes that')
            print('the AI processed before selecting its action: \n', nodes_num)
            print('\n')
            if game_over_out(state):
                print('================Game Over====================')
                print('AI-TREE WIN')
                print('=============================================\n')
                break

            print('===================Below is Ai-1\'s move=====================\n')
            print_func(state)
            print('===================Now This is Baseline AI Turn====================\n \n')

            a,b,c,d = c,d,best_action[0],best_action[1]

            #==============================baseline ai(X)===============================
            if (state[c][d] =="_").any() :
                while True:
                    ramd_move_sub = (random.randint(0,2),random.randint(0,2))
                    if (state[c][d][ramd_move_sub[0]][ramd_move_sub[1]] =="_"):
                        state[c][d][ramd_move_sub[0]][ramd_move_sub[1]] = 'X'
                        break

                if game_over(state[c][d])[0]:
                    state[c][d] =game_over(state[c][d])[1]
                cur_turn = "player"
            else:
                while True:
                    ramd_move = (random.randint(0,2),random.randint(0,2))
                    ramd_move_sub = (random.randint(0,2),random.randint(0,2))
                    if (state[ramd_move[0]][ramd_move[1]][ramd_move_sub[0]][ramd_move_sub[1]] =="_"):
                        state[ramd_move[0]][ramd_move[1]][ramd_move_sub[0]][ramd_move_sub[1]] = 'X'
                        break

                if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                    state[ramd_move[0]][ramd_move[1]] =game_over(state[ramd_move[0]][ramd_move[1]])[1]
                cur_turn = 'player'

            if game_over_out(state):
                print('================Game Over====================')
                print('Baseline ai win')
                print('=============================================\n')
                break

            #print( (state =="_").any())
            #print( game_over_out(state))
            print('===================Below is Ai\'s move=====================\n')
            print_func(state)
            print('===================Now This is Your Turn====================\n \n')

            a,b,c,d = c,d,ramd_move_sub[0],ramd_move_sub[1]


#-====================================================option 1 and option 2============================================
        else:

            #Human turn
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
                    state[a][b] =game_over(state[a][b])[1]
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

        #==========================================TREE AI======================================================
            if choice_ai == 1:
                print('======================1======================')

                unique, counts = np.unique(state[a][b],return_counts=True)
                xo_num = dict(zip(unique,counts))
                unique_sub, counts_sub = np.unique(state[c][d],return_counts=True)
                xo_num_sub = dict(zip(unique_sub,counts_sub))

                nodes_num = 0
                #AI TURN
                if (state[c][d] =="_").any() :

                    if (('X' in xo_num and 'O' in xo_num and xo_num['X'] > xo_num['O']) or
                     ('X' in xo_num and 'O' not in xo_num and xo_num['X']>1)):
                        if '_' in xo_num_sub and xo_num_sub['_'] >1 and state[c][d][a][b] =='_':
                            state[c][d][a][b] = 'P'
                            nodes_num = ai_turn(state[c][d])
                            state[c][d][a][b] ='_'
                        else:
                            nodes_num = ai_turn(state[c][d])
                    else:
                        nodes_num = ai_turn(state[c][d])

                    if game_over(state[c][d])[0]:
                        state[c][d] =game_over(state[c][d])[1]
                    cur_turn = "ai"

                else:
                    #Find a tic-tac-toe which can win by place only one more move
                    for i in range(3):
                        for j in range(3):
                            if (state[i][j] == "_").any():
                                state_temp = state.copy()
                                nodes_num_temp = ai_turn(state_temp[i][j])
                                if game_over(state_temp[i][j])[0]:
                                    nodes_num = ai_turn(state[i][j])
                                    print("random pick")
                                    state[i][j] =game_over(state_temp[i][j])[1]
                                    cur_turn = "ai"
                                    break

                        else: continue
                        break

                    #If did not find that move, we random pick one gird
                    if cur_turn != "ai":
                        print('3')

                        ramd_move = (random.randint(0,2),random.randint(0,2))

                        if (state[ramd_move[0]][ramd_move[1]] =="_").any():
                            nodes_num = ai_turn(state[ramd_move[0]][ramd_move[1]])
                            print("random pick")
                            if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                                state[ramd_move[0]][ramd_move[1]] =game_over(state[ramd_move[0]][ramd_move[1]])[1]
                            cur_turn = "ai"
                        else:
                            for i in range(3):
                                for j in range(3):
                                    if (state[i][j] == "_").any():
                                        nodes_num = ai_turn(state[i][j])
                                        print("random pick")
                                        if game_over(state[i][j])[0]:
                                            state[i][j] =game_over(state[i][j])[1]
                                        cur_turn = "ai"
                                        break
                                else: continue
                                break
                print('the number of tree nodes that')
                print('the AI processed before selecting its action: \n', nodes_num)
                print('\n')
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

        #==========================================option 2 baseline random AI======================================================

            elif(choice_ai == 2):
                print('======================2======================')

                if (state[c][d] =="_").any() :
                    while True:
                        ramd_move = (random.randint(0,2),random.randint(0,2))
                        if (state[c][d][ramd_move[0]][ramd_move[1]] =="_"):
                            state[c][d][ramd_move[0]][ramd_move[1]] = 'O'
                            break

                    if game_over(state[c][d])[0]:
                        state[c][d] =game_over(state[c][d])[1]
                    cur_turn = "ai"
                else:
                    while True:
                        ramd_move = (random.randint(0,2),random.randint(0,2))
                        ramd_move_sub = (random.randint(0,2),random.randint(0,2))
                        if (state[ramd_move[0]][ramd_move[1]][ramd_move_sub[0]][ramd_move_sub[1]] =="_"):
                            state[ramd_move[0]][ramd_move[1]][ramd_move_sub[0]][ramd_move_sub[1]] = 'O'
                            break

                    if game_over(state[ramd_move[0]][ramd_move[1]])[0]:
                        state[ramd_move[0]][ramd_move[1]] =game_over(state[ramd_move[0]][ramd_move[1]])[1]
                    cur_turn = "ai"

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

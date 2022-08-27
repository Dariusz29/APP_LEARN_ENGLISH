# It is a test

# a  = ['a','b','c','d']
# b = ['q','w']


# for i in a, b:
#     if i == a:
#         print('1',i[0:4])
#     elif i == b:
#         print('2',i)

# c=[]
# a = [1,2,3,4,5]
# b = [1,4,6,7,8,9]
# for i in a,b:
#     c.append(i)
# from math import sqrt
# a = 0.508
# b = 0.312

# x = (a*2)**2 + (b*2)**2

# print(sqrt(x)/2.54)

pos_board = {
        1:["X"], 
        2:[0],
        3:[0],
        4:["X"],
        5:[5],
        6:[6],
        7:["X"],
        8:[8],
        9:[9]
    } 
# def rules():
#     x = ("X" or "O")
    

#     if (pos_board[1] and pos_board[2] and pos_board[3])==x:
#         print('You win this game!')
#     elif x == (pos_board[4] and pos_board[5] and pos_board[6]):
#         print('You win this game!')
#     elif x == (pos_board[7] and pos_board[8] and pos_board[9]):
#         print('You win this game!')
#     elif x == (pos_board[1] and pos_board[4] and pos_board[7]):
#         print('You win this game!')
#     elif x == (pos_board[2] and pos_board[5] and pos_board[8]):
#         print('You win this game!')
#     elif x == (pos_board[3] and pos_board[6] and pos_board[9]):
#         print('You win this game!')
#     elif x == (pos_board[1] and pos_board[5] and pos_board[9]):
#         print('You win this game!')
#     elif x == (pos_board[3] and pos_board[5] and pos_board[7]):
#         print('You win this game!')


# x = ["X"] or ["O"]
# z = list(pos_board.values())    
# print(z[3])
# print(z[3] == x)
# if z[0]==x and z[1]==x and z[2]==x:
#     print('You win this game!')

def rules():
        x = ["X"] or ["O"]
        z = list(pos_board.values())
        

        

rules()

# a  = {
#         1:["X"], 
#         2:["X"],
#         3:["X"],
#         4:[4],
#         5:[5],
#         6:[6],
#         7:[7],
#         8:[8],
#         9:[9]
#     } 
# c = True
# while c:
#     for i in a:
#         print(i)
#         if a.index(2) == 3:
#             c = False
#             break
# 
# import random
# ww = ["qwer", 'asdf', 'zxcvbnm']
# pp = ["rewq", 'fdsa', 'mnbvcxz']
# words = random.choice(ww)
# print(words)
# num_ww = ww.index(words)
# num_pp = num_ww
# print(num_ww, num_pp)
# ans = input(f'Type translation {words} = ')


    
# for i, j in zip(pp[num_pp],ans):

#     if ans == pp[num_pp]:
#         print("""
#         Great answer!!!
#         Next phase....""")

#     elif i == j: 
#         print("""
#         Your answer is in half right.
#         Next phase....""")
        
#     else:
#         print("""
#         Bad answer
#         Next phase....""")
                
#     print("Test is finish!")
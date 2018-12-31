board=[' ']*10


def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-------------------------------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-------------------------------')
    print(board[1] + '|'+board[2] + '|' + board[3])


def player_input():
    marker=' '

    while not marker=='x' or marker=='y':
            marker=input('player 1 select your marker')
    if marker=='x':
            return ('x','o')
    else:
            return ('o','x')
def mark(board,marker,position) :
     board[position]=marker

def win(board,marker):
     if(board[7]==marker and board[8]==marker and board[9]==marker or
        board[4] == marker and board[5] == marker and board[6] == marker or
        board[1] == marker and board[2] == marker and board[3] == marker or
        board[7] == marker and board[5] == marker and board[1] == marker or
        board[9] == marker and board[5] == marker and board[3] == marker):
         return True

import random
def choose():
    if random.randint(0,1)==0:
        return 'player 1'
    else:
        return 'player 2'
def space_check(board,position):
    if board[position]==' ':
        return True
    else:
        return False
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice():
    position=' '
    position=int(input('enter your postion'))


    return  position




print('Welcome')






theboard = [' '] * 10
player1_input,player2_input=player_input()
turn=choose()
print(turn+'will play first')
game=True
while game:
          if turn=='player 1':
              print('player1 turn')
              display_board(theboard)
              position=player_choice()
              mark(theboard,player1_input,position)
              if win(theboard,player1_input):
                  display_board(theboard)
                  print('player 1 has won')
                  game=False
                  exit()
              elif full_check(theboard):
                    print('draw')
                    game=False
                    exit()
              else:
                  turn='player 2'
          else:
              print('player2 turn')

              display_board(theboard)
              position = player_choice()
              mark(theboard, player2_input,position)
              if win(theboard, player2_input):
                   display_board(theboard)
                   print('player 2 has won')
                   game = False
                   exit()

              elif full_check(theboard):
                     print('draw')
                     game = False
                     exit()
              else:
                  turn='player 1'

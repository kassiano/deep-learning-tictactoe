
import numpy as np
from random import randint
from neural_network import *


board_char =[[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

board = [[0,0,0],
        [0,0,0],
        [0,0,0]]


def print_board():
    print("********************")
    for i in range(0,3):
        print(board_char[i])
    print("********************")

def end_of_game():

    sum_1_linha = board[0][0] + board[0][1] + board[0][2]
    sum_2_linha = board[0][0] + board[0][1] + board[0][2]
    sum_3_linha = board[0][0] + board[0][1] + board[0][2]

    sum_1_coluna = board[0][0] + board[1][0] + board[2][0]
    sum_2_coluna = board[1][0] + board[1][1] + board[2][1]
    sum_3_coluna = board[2][0] + board[2][1] + board[2][2]

    sum_1_diag = board[0][0] + board[1][1] + board[2][2]
    sum_2_diag = board[0][2] + board[1][1] + board[2][0]

    condicoes = [sum_1_linha , sum_2_linha, sum_3_linha ,
                sum_1_coluna,sum_2_coluna, sum_3_coluna ,
                sum_1_diag, sum_2_diag]

    for i in range(len(condicoes)):

        cond = condicoes[i]
        if(cond == 3):
            print(cond)
            print("Voce ganhou !!")
            return True
        elif (sum_1_linha == 12):
            print("Bot ganhou !!")
            return True

    return False

print("Welcome to the tic tac toe !!")

userToken = "X"
botToken = "O"

print_board()

humanTurn = True


while not end_of_game():

    if (humanTurn):

        linha = int(input("Escolha a linha: "))
        coluna = int(input("Escolha a coluna: "))


        if(board[linha][coluna] == 0):
            board[linha][coluna] = 1
            board_char[linha][coluna] = userToken
            humanTurn = False
            print_board()
        else:
            print("Posicao invalida")

    else:

        linha= randint(0, 2)
        coluna= randint(0, 2)

        if(board[linha][coluna] == 0):
            print("Escolha do bot {},{}".format(linha, coluna))
            board[linha][coluna] = 4
            board_char[linha][coluna] = botToken
            humanTurn = True
            print_board()

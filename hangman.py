#!/usr/bin/env python3

import sys, os, math
# import numpy as np
# import scipy as sp
# import ROOT
# import pyfits as pf

def hangman(word) :
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    o    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome hangman!")

    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board) )
        e = wrong + 1
        print("\n".join(stages[0:e] ))
        if "_" not in board:
            print ("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print ("\n".join(stages[0:wrong+1]) )
        print ("You lose! Answer is {}.".format(word))

hangman("cat")

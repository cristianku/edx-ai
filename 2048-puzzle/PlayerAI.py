import sys
from random import randint
from BaseAI import BaseAI
from Grid import Grid
import numpy as np
import time
from Node import Node
from sys import maxsize
from constants import debug


actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}
class PlayerAI(BaseAI):

  def getMove(self, grid):
    moves = grid.getAvailableMoves()
    max_score = -maxsize
    max_score_move = None
    if debug:
      print  " "
      print " IN MAX -- CREATING CHILD  + number of child  -" \
      + str( len(moves))

    if debug:
      print "   *** starting grid "
      for i in grid.map:
        print("           " + str(i))

    alfa = -maxsize
    beta =  maxsize

    for move in moves:
      child_grid = grid.clone()
      child_grid.move(move)
      if debug:
        print " "
        print " MOVE = " + str(actionDic[move])
        print " MOVE = " + str(actionDic[move])
        print " MOVE = " + str(actionDic[move])
        print " MOVE = " + str(actionDic[move])
        print " MOVE = " + str(actionDic[move])
        print " MOVE = " + str(actionDic[move])

      child_node =  Node(child_grid,  1, "MAX",move,alfa, beta)
      alfa = child_node.alfa
      beta = child_node.beta
      if debug:
        print "   --> score " + str(child_node.get_score())
        print "   --> alfa " + str(alfa)
        print "   --> beta " + str(beta)

      if child_node.alfa > max_score:
          if debug:
            print " ROOT : new max score " \
                  + str(child_node.get_score()) \
                  + " move = " + actionDic[move]
          max_score = child_node.alfa
          max_score_move = move

    if debug:
      print " ** "
      print " ** "
      print " best_move = " + str(actionDic[max_score_move])
      print " ** "
      print " ** "
      exit(0)
    return max_score_move

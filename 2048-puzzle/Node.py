import numpy
from numpy import reshape
from Queue import deque
import copy
from  ComputerAI import ComputerAI
from sys import maxsize
from constants import debug

import Grid
actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}
class Node :
    def __init__(self, grid,  depth, node_type, action=None):
        self._grid = grid
        self._score = 0


        self._depth = depth

        self.action = action

        if action:
            self.printx( " " )
            action_dec = actionDic[action]
            self.printx( "action = " + action_dec)

        action_number = 0
        self.printx( " *************************************** ")
        self.printx( " **************  in depth ******** " + str(self._depth))
        self.printx( " *************************************** ")

        # self._action =  action
        self.children = []
        self._node_type = node_type
        if self._node_type == "MAX":
            self._score = -maxsize
        else:
            self._score = maxsize

        # print " Creating Node of type = " + self._node_type + " depth = " + str(self._depth)
        self.printx("   *** NODE **---> created child (" + self._node_type + ") ")
        for i in self.grid.map:
            self.printx( "           " + str(i))
        #
        self.create_children ()
        # if self._node_type == "Max":
        #     self.score =  -maxsize
        # else:
        #     self.score = maxsize
        #
        # for child in self.children:
        #   print " trying to score children " + str(child.score)
        #     #print self._actions
        #   if self._node_type =="Max":
        #       if child.value < self.score:
        #           self._score = child.score
        #
        #       if self._node_type == "Min":
        #         if child.value > self.score:
        #             self._score = child.score

    def create_children(self):
        if self._depth > 3:
            self._score = self.calculate_score()
            self.printx( " ")
            self.printx( " ---------- LEAF SCORE !!!! " + str(self._score))
            self.printx( " ")
            return
        if self._node_type == "MIN":
            for move in self.grid.getAvailableMoves():
                grid_copy = self._grid.clone()
                grid_copy.move(move)

                new_node_type = "MAX"

                self.children.append(Node(grid_copy,self._depth + 1, new_node_type,move))
            self.printx( "----------- ********* ----------")
            for child in self.children:
                self.printx( " HIER !!! child MINIMUM score " + str(child.score))
                if child.get_score() < self.get_score() :
                    self._score = child.get_score()


        else:
            self.printx( " ******* ")
            self.printx( " SONO IN CICLO DEL MAX")
            self.printx( " ******* ")
            i = - 1
            # CREATING THE OPPONENTS ( PUTTING 2 IN THE FREE CELLS )
            for idx, cell in enumerate(self.grid.getAvailableCells()):
                if idx %2 == 0:
                    grid_copy = self._grid.clone()
                    grid_copy.setCellValue(cell, 2)
                    # print " setting cell value 2"
                    new_node_type = "MIN"
                    i = i + 1
                    self.children.append(Node(grid_copy, self._depth + 1, new_node_type))
                    self.printx( " --> scored : " + str(self.children[i].get_score()))

            self.printx( "----------- ********* ----------")
            for child in self.children:
                a = child.get_score()
                self.printx( " child score " + str(a))
                if child.get_score() > self._score:
                    self._score = child.get_score()
                    self.printx( " ciccio **********!!!!!!")

            self.printx( " ******* ")
            self.printx( " fine IN CICLO DEL MAX -  self._score" + str(self.get_score()))
            self.printx( " ******* ")

    #
    #
    # def __cmp__(self, other):
    #     return cmp(self.priority, other.priority)
    #
    def calculate_score(self):
        score1 = 0.0
        score_total = 0.0
        max_tile = 0.0
        score2 = 0.0
        score3 = 0.0

        for i in self.grid.getAvailableCells():
            score1 = score1 + 1

        max_tile ,max_Tile_Pos  = self.getMaxTileValue()

        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print maxTile
        if    max_Tile_Pos == [0,0] or  max_Tile_Pos == [0, 3] \
           or max_Tile_Pos == [3,0] or  max_Tile_Pos == [3 ,3]:
            score3 = 1
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx( "BINGO !!!!!")
            self.printx("BINGO !!!!!")
            self.printx("BINGO !!!!!")
            self.printx("BINGO !!!!!")
            self.printx("BINGO !!!!!")

        if max_Tile_Pos == [1, 0] or max_Tile_Pos == [1, 1]  or max_Tile_Pos == [0, 1] \
        or max_Tile_Pos == [0, 2] or max_Tile_Pos == [1, 2]  or max_Tile_Pos == [1, 3] :
            score3 = .8
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")
            self.printx("BINGO2 !!!!!")

        score_total = ( score1 / 16) + (max_tile / 16) + score3
        # print " *** score1      " + str(score1) + " - " + str(( score1 / 16))
        # print " *** max_tile    " + str(max_tile)+ " - " + str(( max_tile / 2048))
        # print " *** score_total " + str(score_total )
        return score_total

    def getMaxTileValue(self):
        maxTilePos = 0
        maxTileValue = 0

        for x in xrange(self.grid.size):
          for y in xrange(self.grid.size):
            if self.grid.map[x][y] > maxTileValue:
              maxTileValue = self.grid.map[x][y]
              maxTilePos =  ([x,y])

        return [maxTileValue,maxTilePos]

    @property
    def action(self):
        return self._action


    @property
    def value(self):
        return self._value

    @property
    def score(self):
        return self._score


    def get_score(self):
        return self._score

    @property
    def depth(self):
        return self._depth

    @property
    def grid(self):
        return self._grid

    def printx(self,str):
        if debug:
            bb = " " * (self.depth-1)*5
            print bb + str

    def set_value(self):
        self.value = 0
        for i in self.grid.map:
            self.value = self.value + sum(i)


            #
    #
    # @staticmethod
    # def distance(state, goal):
    #     score = 0
    #     for i in range(len(state)):
    #         if state[i] != goal[i]:
    #             score = score + 1
    #     return score
    #
    #
    # @staticmethod
    # def calculate_priority(x):
    #     aa = (x.depth + TreeNode.manhattan_distance(x.string_state, '012345678'))
    #     return aa
    #
    #
    # @staticmethod
    # def calculate_board_row_from_string(i):
    #     if i in  [0,1,2]: return 1
    #     if i in  [3,4,5]: return 2
    #     if i in  [6,7,8]: return 3
    #
    #
    #
    #
    #
    #
















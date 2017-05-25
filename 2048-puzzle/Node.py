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
    3: "RIGHT",
    99: "COMPUTER "
}
class Node :
    def __init__(self, grid,  depth, node_type, action,alfa, beta ):
        self._grid = grid
        self._score = 0
        self.alfa = alfa
        self.beta = beta

        self._depth = depth

        self.action = action

        if action:
            self.printx( " " )
            action_dec = actionDic[action]
            self.printx( "action = " + action_dec)

        # self._action =  action
        self.children = []
        self.node_type = node_type
        if self.node_type == "MAX":
            self._score = -maxsize
        else:
            self._score = maxsize

        action_number = 0
        self.printx( " ********************************************* ")
        self.printx( " **************  in depth ******** " + str(self._depth) +  " " + self.node_type)
        self.printx( " ********************************************* ")

        # print " Creating Node of type = " + self._node_type + " depth = " + str(self._depth)
        self.printx("   *** NODE **---> created child (" + self.node_type + ") " \
                    + " alfa = " + str(self.alfa) \
                    + " beta = " + str(self.beta))
        # for i in self.grid.map:
        #     self.printx( "           " + str(i))
        #
        self.create_children ()

        print self.node_type

    def create_children(self):
        if self._depth > 2:
            self._score = self.calculate_score()

            self.node_type = "LEAF"

            self.printx( " ")
            self.printx( " ---------- LEAF SCORE !!!! " + str(self._score))
            self.printx( " ")
            return

        i = - 1
        if self.node_type == "MIN":
            self.printx( " ******* ")
            self.printx( " SONO IN CICLO DEL MIN MIN MIN MIN MIN MIN")
            self.printx( " ******* ")
            minUtility = maxsize
            for move in self.grid.getAvailableMoves():
                grid_copy = self._grid.clone()
                grid_copy.move(move)

                new_node_type = "MAX"
                i = i + 1
                self.children.append(Node(grid_copy,self._depth + 1, new_node_type,move, self.alfa, self.beta))


                if self.children[i].node_type == "LEAF":
                    if self.children[i].get_score() < self.beta:
                        self.beta = self.children[i].get_score()
                else:
                    if self.children[i].alfa < self.beta:
                        self.beta = self.children[i].alfa



                if self.alfa >= self.beta:
                     break


            self.printx(" ******* ")
            self.printx(" fine IN CICLO DEL MIN -  self.beta" + str(self.beta))
            self.printx(" ******* ")


        else:
            self.printx( " ******* ")
            self.printx( " SONO IN CICLO DEL MAX")
            self.printx( " ******* ")
            i = - 1
            # CREATING THE OPPONENTS ( PUTTING 2 IN THE FREE CELLS )
            for idx, cell in enumerate(self.grid.getAvailableCells()):
                if i < 3:
                    grid_copy = self._grid.clone()
                    grid_copy.setCellValue(cell, 2)
                    # print " setting cell value 2"
                    new_node_type = "MIN"
                    i = i + 1
                    self.children.append(Node(grid_copy, self._depth + 1, new_node_type,99, self.alfa, self.beta))
                    self.printx( " --> scored : " + str(self.children[i].get_score()))

                    if self.children[i].node_type == "LEAF":
                        if self.children[i].get_score() < self.alfa:
                            self.alfa = self.children[i].get_score()
                    else:
                        if self.children[i].beta > self.alfa:
                            self.alfa = self.children[i].beta

                    if self.alfa <= self.beta:
                        break


            self.printx( " ******* ")
            self.printx( " fine IN CICLO DEL MAX -  self._score" + str(self.get_score()))
            self.printx( " ******* ")

    def calculate_score(self):
        score1 = 0.0
        score_total = 0.0
        max_tile = 0.0
        score2 = 0.0
        score3 = 0.0
        weight1 = 1
        weight2 = 1.5
        weight3 = 1.5

        for i in self.grid.getAvailableCells():
            score1 = score1 + 1

        max_tile, max_Tile_Pos = self.getMaxTileValue()

        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print " !!!!! maxtile  = "
        # print maxTile
        if max_Tile_Pos == [0, 0] or max_Tile_Pos == [0, 3] \
                or max_Tile_Pos == [3, 0] or max_Tile_Pos == [3, 3]:
            score3 = 1
            self.printx("BINGO !!!!!")

        # if max_Tile_Pos == [1, 0] or max_Tile_Pos == [1, 1] or max_Tile_Pos == [0, 1] \
        #         or max_Tile_Pos == [0, 2] or max_Tile_Pos == [1, 2] or max_Tile_Pos == [1, 3]:
        #     score3 = .8
        #     self.printx("BINGO2 !!!!!")

        score_total = (score1 / 16) * weight1 + (max_tile / 16) * weight2 + score3 * weight3
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
        # if debug:
        #      bb = " " * (self.depth-1)*5
        #      print bb + str
        return

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
















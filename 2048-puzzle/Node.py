import numpy
from numpy import reshape
from Queue import deque
import copy
from  ComputerAI import ComputerAI
from sys import maxsize
from constants import debug
from random import randint
import random
import time
import Grid
import math
actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT",
    99: "COMPUTER "
}
defaultProbability = 0.9

maximum_depth = 6

min_child_skip_step = 2

corner1 = [[0,0],
            [3, 0],
            [0, 3],
            [3, 3]
            ]



corner2 = [[0, 1], [0, 2],
           [1, 1], [1, 2],
           [2, 1], [2, 2],
           [3, 1], [3, 2],
           [1, 0],
           [2, 0],
           [1, 3],
           [2, 3],
       ]


class Node :
    def __init__(self, grid,  depth, node_type, action,alfa, beta, start_clock ):
        self._grid = grid
        self._score = 0
        self.alfa = alfa
        self.beta = beta
        self.start_clock = start_clock

        self.possibleNewTiles = [2, 4]

        self.probability = defaultProbability

        self._depth = depth

        self.action = action

        if action:
            action_dec = actionDic[action]

        # self._action =  action
        self.children = []
        self.node_type = node_type
        if self.node_type == "MAX":
            self._score = -maxsize
        else:
            self._score = maxsize

        action_number = 0
        # print  " ********************************************* "
        # print  " **************  in depth ******** " + str(self._depth) +  " " + self.node_type
        # print  " ********************************************* "

        # print " Creating Node of type = " + self._node_type + " depth = " + str(self._depth)
        # for i in self.grid.map:
        #     self.printx( "           " + str(i))
        #
        self.create_children ()



    def create_children(self):
        if self._depth > maximum_depth:
            if self.node_type == "MIN":
                self._score = self.calculate_score()
            else:
                self._score = self.calculate_score()

            self.node_type = "LEAF"

            # print " ---------- LEAF SCORE !!!! " + str(self._score)
            return

        i = - 1
        if self.node_type == "MIN":
            minUtility = maxsize
            for move in self.grid.getAvailableMoves():
                # if i % 2 == 0:
                    grid_copy = self._grid.clone()

                    move_computer = self.getMove_Computer(grid_copy)

                    # # Validate Move
                    if move_computer and grid_copy.canInsert(move_computer):
                        grid_copy.setCellValue(move_computer, self.getNewTileValue())

                    grid_copy.move(move)



                    new_node_type = "MAX"
                    i = i + 1
                    self.children.append(Node(grid_copy,self._depth + 1, new_node_type,move, self.alfa, self.beta,self.start_clock))


                    if self.children[i].node_type == "LEAF":
                        if self.children[i].get_score() < self.beta:
                            self.beta = self.children[i].get_score()
                    else:
                        if self.children[i].alfa < self.beta:
                            self.beta = self.children[i].alfa



                    if self.alfa >= self.beta:
                         break

                # print "  time.clock() - self.start_clock = " + str(time.clock() - self.start_clock)

                    if time.clock() - self.start_clock >= 0.2:
                        break

            # self.printx(" ******* ")
            # self.printx(" fine IN CICLO DEL MIN -  self.beta" + str(self.beta))
            # self.printx(" ******* ")


        else:
            # self.printx( " ******* ")
            # self.printx( " SONO IN CICLO DEL MAX")
            # self.printx( " ******* ")
            i = - 1
            for move in self.grid.getAvailableMoves():

                grid_copy = self._grid.clone()

                move_computer = self.getMove_Computer(grid_copy)

                # Validate Move
                if move_computer and grid_copy.canInsert(move_computer):
                    grid_copy.setCellValue(move_computer, self.getNewTileValue())

                grid_copy.move(move)


                    # for idx, cell in enumerate(cells):
                #     if int(idx) % min_child_skip_step == 0:
                #         grid_copy = self._grid.clone()
                #         grid_copy.setCellValue(cell, self.getNewTileValue())
                        # print " setting cell value 2"
                new_node_type = "MIN"
                i = i + 1
                self.children.append(Node(grid_copy, self._depth + 1, new_node_type,99, self.alfa, self.beta, self.start_clock))
                # self.printx( " --> scored : " + str(self.children[i].get_score()))

                if self.children[i].node_type == "LEAF":
                    if self.children[i].get_score() > self.alfa:
                        self.alfa = self.children[i].get_score()
                else:
                    if self.children[i].beta > self.alfa:
                        self.alfa = self.children[i].beta

                # if self.alfa >= self.beta:
                #     break

                # print "   time.clock() - self.start_clock= " + str(  time.clock() - self.start_clock)

                if time.clock() - self.start_clock >= 0.2:
                    break

            # self.printx( " ******* ")
            # self.printx( " fine IN CICLO DEL MAX -  self._score" + str(self.get_score()))
            # self.printx( " ******* ")

    def calculate_score(self):
        score_total = 0.0
        max_tile = 0.0
        score_corner1 = 0.0
        score_corner2 = 0.0
        score_free_cells = 0
        score_line_ordered = 0
        score_line_ordered_right = 0


        score_line_ordered_left = 0

        weight_free_cells = 10000
        weight_max_tile = 100
        weight_corner = 0.6
        weight_line_ordered = 100
        superbonus = 0

        for idx, i in enumerate(self.grid.map):
            if self.is_sorted(i) and sum(i) > 0 and idx == 0:
                score_line_ordered_right = 1
                if i[0] == i[1] or \
                   i[1] == i[2] or \
                   i[2] == i[3] :
                  superbonus = max(10000, superbonus )

        list_x = []
        for idx, i in enumerate(reversed(self.grid.map)):
            # print i
            list_x = list_x + i
            if self.is_sorted(i) and sum(i) > 0 and idx == 0:
                score_line_ordered_left = 1
        average = sum(list_x) / len(list_x)
        # print str(list_x) + "  AVG = " + str(average)
        # print "*"

        score_line_ordered = max(score_line_ordered_right, score_line_ordered_left)

        for i in self.grid.getAvailableCells():
            score_free_cells = score_free_cells + 1

        max_tile, max_Tile_Pos = self.getMaxTileValue()

        if max_Tile_Pos in corner1:
             weight_corner = 2
        elif max_Tile_Pos in corner2:
             weight_corner = 0.7
        else:
            weight_corner = 0.7

        # score_total = max_tile  * weight_corner  + score_free_cells \
        #               + score_line_ordered_right * 1

        score_total = max_tile * 1000 * weight_corner + score_free_cells

        return score_total


    def printGrid(self):
        for i in self.grid.map:
            print(  str(i))

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


    def getNewTileValue(self):
        if randint(0, 99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1];

    def is_sorted(self,lst, key=lambda x: x):
        for i, el in enumerate(lst[1:]):
            if key(el) < key(lst[i]): # i is the index of the previous element
                return False
        return True

    def getMove_Computer(self, grid):
        # random.seed(9001)

        cells = grid.getAvailableCells()

        return cells[random.randint(0, len(cells) - 1)] if cells else None

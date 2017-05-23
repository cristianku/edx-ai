import sys
from random import randint
from BaseAI import BaseAI
import Minimax
import Minimaxab
from Grid import Grid
import numpy as np
import Helper
import time
from Queue import deque
from Node import Node

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}


class PlayerAI(BaseAI):
        def getMove2(self, grid):
                print " "
                start = time.clock()
                moves = grid.getAvailableMoves()
                max_score = 0
                max_score_move = 0
                max_score_available_cells = 0
                for m in moves:
                    # print ' ***** move *******  ' + actionDic[m]
                    grid_copy = grid.clone()
                    grid_copy.move(m)

                    score = 0
                    for i in grid_copy.map:
                        # print i
                        score = score + sum(i)

                    # print " ---- score !!!: " + str(score)
                    available_cells = grid_copy.getAvailableCells()
                    # print "available cells : " + str( len(available_cells))
                    if score > max_score:
                        # print " score > max_score:" + "score = " + str(score) \
                        #       + "  maxscore = " + str(max_score)
                        max_score_move = m
                        max_score = score
                        max_score_available_cells = len(available_cells)

                    elif score == max_score:
                        # print " score == max_score:" + "score = " + str(score) \
                        #       + "  maxscore = " + str(max_score)
                        if len(available_cells) > max_score_available_cells:
                            max_score_move = m
                            max_score = score
                            max_score_available_cells = len(available_cells)

                    # print ' *****  '

                end = time.clock()
                # print 'time = ' + str(start - end )
                # print float('inf')
                # print " max score " + str(max_score)
                # print " max score move" + actionDic[max_score_move]

                return max_score_move


        def getMove(self, grid):


            self.frontier = deque()
            root = Node(grid)
            # print board_temp_list

            #
            # self.explored = deque()
      #      self.explored.add(self.grid.get_str) to do

            self.frontier.append(root)

            self.nodes_expanded = 0
            self.max_search_depth = 0
            self.possible_actions_list = []
            self.total_time = 0
            self.max_score = 0


            while self.frontier or self.max_search_depth > 4:
                fifo_element = self.frontier.popleft()
                #self.explored.add(fifo_element.string_state) to do

                if fifo_element.get_score >= self.max_score:
                    self.max_score_element = fifo_element


                self.nodes_expanded = self.nodes_expanded + 1
                # print " Expanding node: ... " + str(self.frontier_element.string_state) + " parent actions : " + str(
                #     self.frontier_element.actions)
                # print " Possible actions " + str(functions.get_possible_actions(self.frontier_element.string_state))
                moves = grid.getAvailableMoves()
#                possible_actions_list = list(Resolver.possible_actions(fifo_element.zero_position))
                #
                # for self.index, self.action in enumerate(self.possible_actions_list):
                #     start_time = time.time()
                #
                #     end_time = time.time()
                #     self.total_time = self.total_time + end_time - start_time
                for action in moves:
                    grid_copy = grid.clone()
                    grid_copy.move(action)
                    child_node = Node(grid_copy.move(action), action=action, parent=fifo_element)

                    if child_node.depth > self.max_search_depth:
                        self.max_search_depth = child_node.depth

                    # if self.child_node.string_state not in self.explored:
               #     if child_node.string_state not in self.explored:
                    self.frontier.append(child_node)
                    # self.explored.append(self.child_node.string_state)
                    # print " appending explored " + self.child_node.string_state
#                    self.explored.add(child_node.string_state)
                    # print "   child_node.string_state = " + str(self.child_node.string_state)
                    # print "   child_node.path_steps   = " + str(self.child_node.path_steps)
                    # print "   child_node.actions      = " + str(self.child_node.actions)
                    # print " "

                return self.max_score_element.action

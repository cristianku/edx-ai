import numpy
from numpy import reshape
from Queue import deque
import copy

import Grid

class Node :
    def __init__(self, grid,  action = None,  parent=None, if_priority=None, counter =None):
        self._grid = grid
        action_number = 0
        if parent:
            self._depth = parent.depth + 1

            self._action =  action

            if if_priority:
                self._priority = Node.calculate_priority(self) * 1000000 + counter



             #print self._actions
        else:
             self._depth = 0
             if if_priority:
                 self._priority = Node.calculate_priority(self)* 1000000 + counter


    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    def get_score(self):
        score = 0
        for i in self.grid.map:
            # print i
            score = score + sum(i)
        return score

    @property
    def priority(self):
        return self._priority


    @property
    def action(self):
        return self._action


    @property
    def grid(self):
        return self._grid


    @property
    def depth(self):
        if self._depth: return len(self._depth)
        else: return 0


    @staticmethod
    def distance(state, goal):
        score = 0
        for i in range(len(state)):
            if state[i] != goal[i]:
                score = score + 1
        return score


    @staticmethod
    def calculate_priority(x):
        aa = (x.depth + TreeNode.manhattan_distance(x.string_state, '012345678'))
        return aa


    @staticmethod
    def calculate_board_row_from_string(i):
        if i in  [0,1,2]: return 1
        if i in  [3,4,5]: return 2
        if i in  [6,7,8]: return 3


    @staticmethod
    def calculate_board_col_from_string(i):
        if i in [0, 3, 6]: return 1
        if i in [1, 4, 7]: return 2
        if i in [2, 5, 8]: return 3


    @staticmethod
    def manhattan_distance(state, goal):
        score = 0
        for i in range(len(state)):
            if state[i] != "0":
                origin_char = state[i]
                goal_position = goal.index(origin_char)
                goal_row = TreeNode.calculate_board_row_from_string(goal_position)
                goal_col = TreeNode.calculate_board_col_from_string(goal_position)

                origin_row = TreeNode.calculate_board_row_from_string(i)
                origin_col = TreeNode.calculate_board_col_from_string(i)
                score = score + abs(goal_row - origin_row) + abs( goal_col - origin_col)
        return score


























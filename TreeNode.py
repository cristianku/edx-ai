import numpy
from numpy import reshape
from Queue import deque
import copy

class TreeNode :
    def __init__(self, string_state, action =None,  parent=None, if_priority=None):
        self._string_state = string_state
        self._zero_position = string_state.index("0")
        action_number = 0
        if parent:
             self._actions = parent.actions
             self._actions = self._actions +  action

             self._path_steps = parent.path_steps + 1
             if if_priority:
                self._priority = TreeNode.calculate_priority(self)


             #print self._actions
        else:
             self._string_state = string_state
             self._zero_position = string_state.index("0")
             self._actions = ""
             self._path_steps = 0
             if if_priority:
                 self._priority = TreeNode.calculate_priority(self)


    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    @property
    def priority(self):
        return self._priority

    @property
    def zero_position(self):
        return self._zero_position

    @property
    def actions(self):
        return self._actions

    @property
    def path_steps(self):
        return self._path_steps

    @property
    def string_state(self):
        return self._string_state


    @property
    def depth(self):
        if self._actions: return len(self._actions)
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
        aa = (x.depth + TreeNode.distance(x.string_state, '012345678'))
        return aa


    @staticmethod
    def manhattan_distance(state, goal):
        score = 0
        for i in range(len(state)):
            origin_char = state[i]
            goal_position = goal.index(origin_char)
            if i in range(0,2):
                row = 1
            elif i in range( 3,5)
            if state[i] != goal[i]:
                score = score + 1
        return score



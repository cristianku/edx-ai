import numpy
from numpy import reshape
from Queue import deque
import copy

class TreeNode :
    def __init__(self, string_state, action =None,  parent=None):
        self._string_state = string_state
        self._zero_position = string_state.index("0")
        action_number = 0
        if parent:
             self._actions = list(parent.actions[:])

             if len(self._actions)    < 100000:
                 self._actions.append(action)

             self._path_steps = parent.path_steps + 1

             #print self._actions
        else:
             self._string_state = string_state
             self._zero_position = string_state.index("0")
             self._actions = [] #numpy.array([])
             self._path_steps = 0


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
        return len(self._actions)  # to account for 0 indexing


class TreeNode :
    def __init__(self, string_state, action =None,  parent=None):
        self._string_state = string_state
        if parent:
         self._actions = list(parent.actions)
         self._actions.append(action)
         self._path_steps = parent.path_steps + 1
        else:
         self._string_state = string_state
         self._actions = []
         self._path_steps = 0


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

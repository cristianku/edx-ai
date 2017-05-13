class TreeNode :
    def __init__(self, string_state, action =None,  parent=None):
        self.string_state = string_state
        if parent:
         self.actions = parent.actions
         self.actions.append(action)
         self.path_steps = parent.path_steps + 1
        else:
         self.string_state = string_state
         self.actions = []
         self.path_steps = 0


    @property
    def string_state(self):
        return self.string_state

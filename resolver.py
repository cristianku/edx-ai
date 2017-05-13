from TreeNode import TreeNode
from Queue import deque
import functions

class Resolver:
    def __init__(self, input_board_str):
        self.start_board_str = input_board_str
        self.final_board_str = ""
        self.path_steps = 0
        self.depth = 0
        self.actions = []
        self.max_search_depth = 0
        self.nodes_expanded = 0
        self.goal_state =  '012345678'


    def bfs_Solve(self):
        root = TreeNode(string_state=self.start_board_str)
        # print board_temp_list

        #
        self.explored = deque()
        self.explored.append(root.string_state)

        self.fifo = deque()
        self.fifo.append(root)

        self.nodes_expanded = 0
        self.max_search_depth = 0

        while self.fifo:
            self.fifo_element = self.fifo.popleft()
            self.explored.append(self.fifo_element.string_state)
            if self.fifo_element.string_state == self.goal_state:
                print " -- FOUND THE ELEMENT !!!!"
                self.path_steps = self.fifo_element.path_steps
                self.depth = self.fifo_element.depth
                self.actions = self.fifo_element.actions


            self.nodes_expanded = self.nodes_expanded + 1

            print " Expanding node: ... " + str(self.fifo_element.string_state) + " parent actions : " + str(
                self.fifo_element.actions)
            print " Possible actions " + str(functions.get_possible_actions(self.fifo_element.string_state))
            for possible_action in functions.get_possible_actions(self.fifo_element.string_state):

                move_str = functions.make_move(self.fifo_element.string_state, possible_action)
                child_node = TreeNode(string_state=move_str, action=possible_action, parent=self.fifo_element)

                print "   child_node.string_state = " + str(child_node.string_state)
                print "   child_node.path_steps   = " + str(child_node.path_steps)
                print "   child_node.actions      = " + str(child_node.actions)
                print " "
                if child_node.depth > max_search_depth:
                    max_search_depth = child_node.depth
                if (child_node.string_state not in self.explored):
                    self,fifo.append(child_node)

            if self.nodes_expanded > 50: break

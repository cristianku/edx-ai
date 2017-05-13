from TreeNode import TreeNode
from Queue import deque
import functions

class Resolver:
    def __init__(self, input_board_str):
        self.start_board_str = input_board_str
        self.goal_state =  '012345678'


    def bfs_Solve(self):
        root = TreeNode(string_state=self.start_board_str)
        # print board_temp_list

        #
        self.explored = deque()
        self.explored.append(self.start_board_str)

        self.fifo = deque()
        self.fifo.append(root)

        self.nodes_expanded = 0
        self.max_search_depth = 0

        while self.fifo:
            self.fifo_element = self.fifo.popleft()
            self.explored.append(self.fifo_element.string_state)
            if self.fifo_element.string_state == self.goal_state:
                print " -- FOUND THE ELEMENT !!!!"
                self.path_to_goal = self.fifo_element.actions
                self.cost_of_path = self.fifo_element.path_steps
                self.search_depth = self.fifo_element.path_steps
                # self.max_search_depth

                break

            self.nodes_expanded = self.nodes_expanded + 1
            # print " Expanding node: ... " + str(self.fifo_element.string_state) + " parent actions : " + str(
            #     self.fifo_element.actions)
            # print " Possible actions " + str(functions.get_possible_actions(self.fifo_element.string_state))
            for self.possible_action in functions.get_possible_actions(self.fifo_element.string_state):

                self.move_str = functions.make_move(self.fifo_element.string_state, self.possible_action)
                self.child_node = TreeNode(string_state=self.move_str, action=self.possible_action, parent=self.fifo_element)

                if self.child_node.depth > self.max_search_depth:
                    self.max_search_depth = self.child_node.depth

                if self.child_node.string_state not in self.explored:
                    self.fifo.append(self.child_node)
                    # print "   child_node.string_state = " + str(self.child_node.string_state)
                    # print "   child_node.path_steps   = " + str(self.child_node.path_steps)
                    # print "   child_node.actions      = " + str(self.child_node.actions)
                    # print " "


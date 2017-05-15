from TreeNode import TreeNode
from Queue import deque
import functions
import numpy
import time

class Resolver:
    def __init__(self, input_board_str):
        self.start_board_str = input_board_str
        self.goal_state =  '012345678'
        self.path_to_goal = []
        self.cost_of_path = 0

        self.search_depth = 0
        self.tree_node_creation = 0

        self.explored = set()

        self.fifo = deque()

        self.nodes_expanded = 0

        self.max_search_depth = 0


    @staticmethod
    def swapchar(text, fst, snd):
        ba = bytearray(text)
        ba[fst], ba[snd] = ba[snd], ba[fst]
        return ba

    @staticmethod
    def possible_actions(zero_position):
        possible_actions = []

        if 3 <= zero_position <= 8:
            possible_actions.append("U")

        if 0 <= zero_position <= 5:
            possible_actions.append("D")

        if zero_position in [1, 2, 4, 5, 7, 8]:
            possible_actions.append("L")

        if zero_position in [0, 1, 3, 4, 6, 7]:
            possible_actions.append("R")

        return possible_actions

    @staticmethod
    def make_move_str(string_state,zero_position, direction):
        to_position = zero_position
        if direction == "L":
            to_position = zero_position - 1

        elif direction == "R":
            to_position = zero_position + 1

        elif direction == "U":
            to_position = zero_position - 3

        elif direction == "D":
            to_position = zero_position + 3

        # print "zero_position_row_new " + str(zero_position_row_new)
        # print "zero_position_col_new "  + str(zero_position_col_new)

        # b_string_state = bytearray(string_state)
        # #b_string_state = list(string_state)
        # b_string_state[zero_position] = b_string_state[to_position]
        # b_string_state[to_position] = "0"
        return str(Resolver.swapchar(string_state, to_position, zero_position ))
        # b_string_state)

    def bfs_Solve(self):
        root = TreeNode(string_state=self.start_board_str)
        # print board_temp_list

        #
        # self.explored = deque()
        self.explored.add(self.start_board_str)

        self.fifo.append(root)

        self.nodes_expanded = 0
        self.max_search_depth = 0
        self.possible_actions_list = []
        self.total_time = 0

        while self.fifo:
            fifo_element = self.fifo.popleft()
            self.explored.add(fifo_element.string_state)

            if fifo_element.string_state == self.goal_state:
                # print " -- FOUND THE ELEMENT !!!!"

                self.path_to_goal = list(fifo_element.actions)
                # print self.path_to_goal
                for idx, item in enumerate(self.path_to_goal):
                    if "L" in item:
                        item = "Left"
                        self.path_to_goal[idx] = item
                    if "R" in item:
                            item = "Right"
                            self.path_to_goal[idx] = item
                    if "U" in item:
                        item = "Up"
                        self.path_to_goal[idx] = item
                    if "D" in item:
                        item = "Down"
                        self.path_to_goal[idx] = item

                self.cost_of_path = fifo_element.path_steps
                self.search_depth = fifo_element.path_steps
                # self.max_search_depth

                break

            self.nodes_expanded = self.nodes_expanded + 1
            # print " Expanding node: ... " + str(self.fifo_element.string_state) + " parent actions : " + str(
            #     self.fifo_element.actions)
            # print " Possible actions " + str(functions.get_possible_actions(self.fifo_element.string_state))

            possible_actions_list = list(Resolver.possible_actions(fifo_element.zero_position))
            #
            # for self.index, self.action in enumerate(self.possible_actions_list):
            #     start_time = time.time()
            #
            #     end_time = time.time()
            #     self.total_time = self.total_time + end_time - start_time
            for action in possible_actions_list:

                move_str = Resolver.make_move_str( fifo_element.string_state, fifo_element.zero_position, action)
                child_node = TreeNode(string_state=move_str, action=action, parent=fifo_element)

                if child_node.depth > self.max_search_depth:
                    self.max_search_depth = child_node.depth

                # if self.child_node.string_state not in self.explored:
                if child_node.string_state not in self.explored:
                    self.fifo.append(child_node)
                    # self.explored.append(self.child_node.string_state)
                    # print " appending explored " + self.child_node.string_state
                    self.explored.add(child_node.string_state)
                    # print "   child_node.string_state = " + str(self.child_node.string_state)
                    # print "   child_node.path_steps   = " + str(self.child_node.path_steps)
                    # print "   child_node.actions      = " + str(self.child_node.actions)
                    # print " "


    def dfs_Solve(self):
        root = TreeNode(string_state=self.start_board_str)
        # print board_temp_list

        #
        # self.explored = deque()
        self.explored.add(self.start_board_str)

        self.fifo.append(root)

        self.nodes_expanded = 0
        self.max_search_depth = 0
        self.possible_actions_list = []
        self.total_time = 0

        while self.fifo:
            fifo_element = self.fifo.pop()
            # print " fifo_element " + fifo_element.string_state
            self.explored.add(fifo_element.string_state)

            if fifo_element.string_state == self.goal_state:
                # print " -- FOUND THE ELEMENT !!!!"

                self.path_to_goal = list(fifo_element.actions)
                # print self.path_to_goal
                for idx, item in enumerate(self.path_to_goal):
                    if "L" in item:
                        item = "Left"
                        self.path_to_goal[idx] = item
                    if "R" in item:
                        item = "Right"
                        self.path_to_goal[idx] = item
                    if "U" in item:
                        item = "Up"
                        self.path_to_goal[idx] = item
                    if "D" in item:
                        item = "Down"
                        self.path_to_goal[idx] = item

                self.cost_of_path = fifo_element.path_steps
                self.search_depth = fifo_element.path_steps
                # self.max_search_depth

                break

            self.nodes_expanded = self.nodes_expanded + 1
            # print " Expanding node: ... " + str(self.fifo_element.string_state) + " parent actions : " + str(
            #     self.fifo_element.actions)
            # print " Possible actions " + str(functions.get_possible_actions(self.fifo_element.string_state))

            possible_actions_list = list(Resolver.possible_actions(fifo_element.zero_position))
            #
            # for self.index, self.action in enumerate(self.possible_actions_list):
            #     start_time = time.time()
            #
            #     end_time = time.time()
            #     self.total_time = self.total_time + end_time - start_time
            for action in list(reversed(possible_actions_list)):

                move_str = Resolver.make_move_str(fifo_element.string_state, fifo_element.zero_position, action)
                child_node = TreeNode(string_state=move_str, action=action, parent=fifo_element)

                if child_node.depth > self.max_search_depth:
                    self.max_search_depth = child_node.depth

                # if self.child_node.string_state not in self.explored:
                if child_node.string_state not in self.explored:
                    self.fifo.append(child_node)
                    # self.explored.append(self.child_node.string_state)
                    # print " appending explored " + self.child_node.string_state
                    self.explored.add(child_node.string_state)
                    # print "   child_node.string_state = " + str(self.child_node.string_state)
                    # print "   child_node.path_steps   = " + str(self.child_node.path_steps)
                    # print "   child_node.actions      = " + str(self.child_node.actions)
                    # print " "

import sys
from numpy import reshape
import numpy
from Queue import deque
from TreeNode import TreeNode
import functions

goal_state =  numpy.array('012345678')

# print " goal_state = "
# print goal_state

initial_board = sys.argv[2].split(',')
board_temp_string = ''.join(initial_board)
# print board_temp_string
board_temp_list = list(board_temp_string)

root = TreeNode(string_state=board_temp_string)
# print board_temp_list

#
explored = deque()
explored.append ( root.string_state)

fifo = deque()
fifo.append ( root)

print root.string_state
nodes_expanded = 0

while fifo:
    fifo_element = fifo.popleft()
    nodes_expanded = nodes_expanded + 1
    move_up_str = functions.make_move(fifo_element.string_state, "UP")
    print move_up_str
    child_node = TreeNode ( string_state = move_up_str, action = "UP", parent= fifo_element )
    print " Create a child from " + str(fifo_element.string_state) + " parent actions : " + str(fifo_element.actions)
    print "   child_node.string_state = "  + str(child_node.string_state)
    print child_node.path_steps
    print child_node.actions
import sys
from numpy import reshape
import numpy
from Queue import deque
from TreeNode import TreeNode
import functions
import resolver

# print " goal_state = "
# print goal_state

initial_board = sys.argv[2].split(',')
board_temp_string = ''.join(initial_board)
# print board_temp_string
board_temp_list = list(board_temp_string)

# print board_temp_list


solve_bfc = resolver.Resolver(board_temp_string)
solve_bfc.bfs_Solve()

print "   GOAL.string_state     = " + str(solve_bfc.string_state)
print "   GOAL.path_steps       = " + str(solve_bfc.path_steps)
print "   GOAL.depth            = " + str(solve_bfc.depth)
print "   GOAL.actions          = " + str(solve_bfc.actions)
print "   max_search_depth      = " + str(solve_bfc.max_search_depth)
print "   nodes expanded        = " + str(solve_bfc.nodes_expanded)



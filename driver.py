import sys
from numpy import reshape
import numpy
from Queue import deque
from TreeNode import TreeNode
import functions
import resolver
import time
import resource
from sys import platform

print platform


# print " goal_state = "
# print goal_state

initial_board = sys.argv[2].split(',')
board_temp_string = ''.join(initial_board)
# print board_temp_string
board_temp_list = list(board_temp_string)

# print board_temp_list

initial_time = time.time()
solve_bfc = resolver.Resolver(board_temp_string)
solve_bfc.bfs_Solve()
final_time = time.time()

print "   GOAL.path_to_goal           = " + str(solve_bfc.path_to_goal)
print "   GOAL.cost_of_path           = " + str(solve_bfc.cost_of_path)
print "   nodes expanded              = " + str(solve_bfc.nodes_expanded)
print "   GOAL.search_depth           = " + str(solve_bfc.search_depth)
print "   GOAL.max_search_depth       = " + str(solve_bfc.max_search_depth)
print "   running time                = " + str(final_time - initial_time)

if platform == "darwin":
    # linux
    memory_usage_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
else:
    memory_usage_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024

print "   max_ram_usage               = " + str(memory_usage_mb)
print ""



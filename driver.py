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

# import cProfile as profile

# # In outer section of code
# pr = profile.Profile()
# pr.disable()
#
# # In section you want to profile
# pr.enable()
#

# print " goal_state = "
# print goal_state
solver_type  = sys.argv[1].split(',')[0].upper()

initial_board = sys.argv[2].split(',')
board_temp_string = ''.join(initial_board)
# print board_temp_string

board_temp_list = list(board_temp_string)
solver = resolver.Resolver(board_temp_string)

# print board_temp_list

initial_time = time.time()
# print solver_type

if solver_type  == "BFS" :
    solver.bfs_Solve()
elif solver_type  == "DFS" :
    solver.dfs_Solve()
elif solver_type  == "AST" :
    solver.a_Star_Solve()

final_time = time.time()
#
# print "   GOAL.path_to_goal           = " + str(solver.path_to_goal)
# print "   GOAL.cost_of_path           = " + str(solver.cost_of_path)
# print "   nodes expanded              = " + str(solver.nodes_expanded)
# print "   GOAL.search_depth           = " + str(solver.search_depth)
# print "   GOAL.max_search_depth       = " + str(solver.max_search_depth)
# # print " total time spent "  + '{:.16f}'.format(solve_bfc.total_time)
# print " total running time "  + str(int(final_time -  initial_time))

if platform == "darwin":
    # linux
    memory_usage_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024
else:
    memory_usage_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
#
# print "   max_ram_usage               = " + str(memory_usage_mb)
# print ""

with open('output.txt', 'w+') as f:
    f.write("path_to_goal: "     + str(solver.path_to_goal) +  "\n")
    f.write("cost_of_path: "     + str(solver.cost_of_path) +  "\n")
    f.write("nodes_expanded: "   + str(solver.nodes_expanded) +  "\n")
    f.write("search_depth: "     + str(solver.search_depth) +  "\n")
    f.write("max_search_depth: " + str(solver.max_search_depth) +  "\n")
    f.write("running_time: "     + '{:.6f}'.format(final_time -  initial_time) + "\n")
    f.write("max_ram_usage: "    + str(memory_usage_mb) )

# code of interest
# pr.disable()

# Back in outer section of code
# pr.dump_stats('profile.pstat')



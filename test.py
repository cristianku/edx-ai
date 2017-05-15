import time
from TreeNode import TreeNode
from Queue import deque
from  resolver import Resolver

start = time.time()
explored = deque()
fifo = deque()
a = 0
child_node1 = TreeNode(string_state="012345678", action="Up")

for i in range ( 0,1000000):
   child_node = TreeNode(string_state="012345678", action="Up",parent = child_node1)
   explored.append("012345678")
   if "012345678" in explored:
      a = a + 1
   Resolver.swapchar("012345678",3,5)
   possible_actions = Resolver.possible_actions(3)
   Resolver.make_move_str("012345678",4,"Up")
   Resolver.make_move_str("012345678", 4, "Up")
   Resolver.make_move_str("012345678", 4, "Up")
   Resolver.make_move_str("012345678", 4, "Up")

end = time.time()

print " total processing time = " + str(end - start )
print "total fifo search "  + str(a)
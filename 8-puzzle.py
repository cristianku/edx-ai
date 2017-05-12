#1,2,5,3,4,0,6,7,8
import sys
from sys import getsizeof
from numpy import reshape
import numpy
from Queue import deque
import Queue

def swap_cells(array_2d,from_row, from_col, to_row, to_col ):
#    print "swaping cells from row " + str (from_row)
#    print "swaping cells from col " + str (from_col)
#    print "swaping cells to row   " + str (to_row)
#    print "swaping cells to col   " + str (to_col)
    new_array = numpy.array(array_2d)

    value_1 = array_2d[from_row, from_col]
    value_2 = array_2d[to_row, to_col]
    new_array[from_row, from_col] = value_2
    new_array[to_row, to_col] = value_1

    return new_array


def make_move(element_string, direction ):
   np_array_input = to_table(element_string)
   zero_position = numpy.where( np_array_input == "0" )

   # print " zero position !!!!!!  " + str(zero_position)
   zero_position_row =  zero_position[0]
   zero_position_col =  zero_position[1]
   # print zero_position_row
   # print zero_position_col

   if direction == "LEFT" :
      zero_position_row_new = zero_position_row
      zero_position_col_new = zero_position_col - 1

   elif direction == "RIGHT" :
      zero_position_row_new = zero_position_row
      zero_position_col_new = zero_position_col + 1

   elif direction == "UP" :
      zero_position_row_new = zero_position_row - 1
      zero_position_col_new = zero_position_col

   elif direction == "DOWN" :
      zero_position_row_new = zero_position_row + 1
      zero_position_col_new = zero_position_col

   # print "zero_position_row_new " + str(zero_position_row_new)
   # print "zero_position_col_new "  + str(zero_position_col_new)

   if  not (( 0 <= zero_position_row_new  <= 2 )  and
       ( 0 <= zero_position_col_new  <= 2 ) ) :
     # print " move not possible "
     new_array = numpy.array([])

   else:
     new_array = swap_cells(np_array_input,zero_position_row,zero_position_col,zero_position_row_new, zero_position_col_new)

   # print "array found :::::"
   #
   # print new_array

   if new_array.size > 0 :
     new_array_str = to_string(new_array)
     return new_array_str
   else:
     return ""



# example of
# possible moves:

#   MOve RIGHT
#              [[0,1,2],                     [[1,0,2],
#               [3,4,5],             -->      [3,4,5],
#               [6,7,8]]                      [6,7,8]]

#   MOves LEFT     ( NOT POSSIBLE ! )
#              [[0,1,2],
#               [3,4,5],             -->
#               [6,7,8]]


#   MOve up ( NOT POSSIBLE ! )
#              [[0,1,2],                     [[1,0,2],
#               [3,4,5],             -->      [3,4,5],
#               [6,7,8]]                      [6,7,8]]

#   MOve down
#              [[0,1,2],                     [[3,1,2],
#               [3,4,5],             -->      [0,4,5],
#               [6,7,8]]                      [6,7,8]]

def to_table(input_string):
    # print " ****** to_table "
    # print " ****** input_string "
    # print input_string
    # print type(input_string)
    # print "splitting "
    input_list = numpy.array(list(input_string))

    list_numpy_reshaped = reshape (input_list, (3,3) )
    return list_numpy_reshaped

def to_string(input_numpy_array):
    # print " ************ to string "
    # print " ************ to string "
    # print " ************ to string "
    # print " ************ to string "
    # print " ************ to string "
    # print " ************ to string "
    # print input_numpy_array
    # print type(input_numpy_array)
    input_numpy_array_reshaped = list(reshape(input_numpy_array,(9)))
    final_string = ""
    for x in input_numpy_array_reshaped:
        final_string = final_string + x

    # print final_string
    return  final_string


goal_state =  numpy.array('012345678')

# print " goal_state = "
# print goal_state

initial_board = sys.argv[1].split(',')
board_temp_string = ''.join(initial_board)
# print board_temp_string
board_temp_list = list(board_temp_string)

# print board_temp_list


#print initial_board

#print board

#make_moves(initial_board)

# BFS

#explored = numpy.array(frontier)
#explored.shape = (1,3,3)

explored = deque()
path = deque()
#print " explored "
#print explored
# print initial_board
# print to_string(initial_board)
#
# print numpy.array(to_string(initial_board))

print " ####################### "
print " ####################### "
print " #####     initial_board"
print to_table(initial_board)
print " ####################### "
tmp = to_string(initial_board)
tmp2 =  [tmp  ,  "root",0,0, 0]

fifo = deque()
fifo.append (tmp2)
cycle = 0
print  " "

node_number = 0
search_dept = 0
while  fifo:
  search_dept = search_dept + 1
  print " *************  FIFO ************ "
  print fifo
  print " *************  FIFO ************ "
  # print " sono qui "
  fifo_element =  fifo.popleft()
  # print "fifo_element"
  # print fifo_element

  explored.append((fifo_element, fifo_element[2]))
  # print " *************  explored ************ "
  # print explored
  # print " *************  explored ************ "
  # print " ----------------child = make_move_left(b) "

  # print "testing fifo_element if == goal_State "
  fifo_element_str = fifo_element[0]
  # print to_table(fifo_element_str)
  print " "
  if len(fifo_element_str) > 0 :
      if fifo_element_str  == goal_state:
         path.append(fifo_element)
         print "GOAL REACHED !!!!!"
         break
  #
  #
  #     print " fifo_element_2 " + fifo_element_2
  #     print getsizeof(fifo_element_2)
      child = make_move(fifo_element_str, "LEFT")
      # print " child extracted going left " + child +  "( length = ) "  +  str(len(child))
      if len(child)> 0:
       if not ((child in fifo) or ( child in explored)):
           node_number = node_number + 1
           fifo.append([child, "LEFT",node_number, fifo_element[2],search_dept])

      child = make_move(fifo_element_str, "RIGHT")
      # print " child extracted going right " + child + "( length = ) " + str(len(child))
      if len(child) > 0:
       if not ((child in fifo) or (child in explored)):
           node_number = node_number + 1
           fifo.append([child, "RIGHT",node_number,fifo_element[2],search_dept])

      child = make_move(fifo_element_str, "UP")
      # print " child extracted going UP " + child + "( length = ) " + str(len(child))
      if len(child) > 0:
        if not ((child in fifo) or (child in explored)):
            node_number = node_number + 1
            fifo.append([child, "UP",node_number,fifo_element[2],search_dept])

      child = make_move(fifo_element_str, "DOWN")
      # print " child extracted going DOWN " + child + "( length = ) " + str(len(child))
      if len(child) > 0:
        if not ((child in fifo) or (child in explored)):
            node_number = node_number + 1
            fifo.append([child, "DOWN",node_number,fifo_element[2],search_dept])


      print " "

      #     print "fifo "
  #     print fifo
  #     print  " "
  # exit()


# print " ***** explored :"
# while explored:
#   print explored.popleft()
print ""
print ""
print ""
print " S T A T I S T I C S "
print " #######   "
print " ####### initial board "
print initial_board
print " #######   "
print " "
print " FIFO  "
print fifo
print " "
print " explored  "
print explored
# reconstruction of Tree
path = deque()
a = explored.pop()
path.appendleft(a)
parent_number_previous = a[0][3]

nodes_expanded = 0
while explored:
  a = explored.pop()
  nodes_expanded = nodes_expanded + 1
  # so the parent number of the previous is my self
  if parent_number_previous == a[0][2]:
    path.appendleft(a)
    parent_number_previous = a[0][3]
  # print " node value " + str( a[0][0])
  # print " move " + str( a[0][1])
  # print " node_number " + str(a[0][2])
  # print " parent_number " + str(a[0][3])

nodes_expanded = nodes_expanded -1
print " "
print " "
print " $$$$$$$$$$$$$$$$$$ PATH %%%%%%%%%%%%%%%%%"
print path
cost_of_path = 0
while path:
    a = path.popleft()
    cost_of_path = cost_of_path + 1

cost_of_path = cost_of_path -1
print " COST OF PATH   : " + str( cost_of_path)
print " NODES EXPANDED : " + str( nodes_expanded)
print " search dept    :"  + str(search_dept)

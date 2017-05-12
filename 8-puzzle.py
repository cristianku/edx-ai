import sys
from numpy import reshape
import numpy
from collections import deque

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


def make_move_array(array_2d, direction):
   print "make_move_array   !!!!!!!!!!"
   print array_2d
   zero_position = numpy.where( array_2d == "0" )

   print " zero position !!!!!!  " + str(zero_position)
   zero_position_row =  zero_position[0]
   zero_position_col =  zero_position[1]
   print zero_position_row
   print zero_position_col

#  zero_position_x =   numpy.str(zero_position[0])
 #  zero_position_y =   zero_position[1]


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

   print "zero_position_row_new " + str(zero_position_row_new)
   print "zero_position_col_new "  + str(zero_position_col_new)

   if  not (( 0 <= zero_position_row_new  <= 2 )  and
       ( 0 <= zero_position_col_new  <= 2 ) ) :
     print " move not possible "
     a = numpy.array([])
     return a

   else:
     new_array = swap_cells(array_2d,zero_position_row,zero_position_col,zero_position_row_new, zero_position_col_new)

     return numpy.array(new_array)

def make_move_right(array_2d ):


   # MOVE RIGHT
   print " ***** "
   print " ******   board -- making move to the right "
   print " ***** "

   array_right =  make_move_array(array_2d, "RIGHT")
   if array_right.size > 0 :

     return array_right
   else:
     return numpy.array([])

def make_move_left(array_2d ):

   # MOVE left
   print " ***** "
   print " ******   board -- making move to the LEFT "
   print " ***** "

   array_left =  make_move_array(array_2d, "LEFT")
   if array_left.size > 0 :
     return array_left
   else:
     return numpy.array([])

def make_move_up(array_2d ):


   # MOVE UP
   print " ***** "
   print " ******   board -- making move UP "
   print " ***** "

   array_up =  make_move_array(array_2d, "UP")
   if array_up.size > 0 :
     return array_up
   else:
     return numpy.array([])

def make_move_down(array_2d ):

   # MOVE DOWN
   print " ***** "
   print " ******   board -- making move DOWN "
   print " ***** "

   array_down =  make_move_array(array_2d, "DOWN")
   if array_down.size > 0 :
     return array_down
   else:
     return numpy.array([])



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


goal_state =  [[0,1,2],
               [3,4,5],
               [6,7,8]]

board_temp = sys.argv[1].split(',')

initial_board = reshape (board_temp, (3,3) )

#print initial_board

#print board

#make_moves(initial_board)

# BFS

frontier = numpy.array(initial_board)
frontier.shape = (1,3,3)
#explored = numpy.array(frontier)
#explored.shape = (1,3,3)

explored = deque()
#print " explored "
#print explored

fifo = deque(frontier)
while fifo:
  fifo_element =  fifo.popleft()
  explored.append(fifo_element)
  print " ----------------child = make_move_left(b) "

  child = make_move_left(fifo_element)
  if child.size > 0:
   fifo.append(child)

  child = make_move_right(fifo_element)
  if child.size > 0:
    fifo.append(child)

  child = make_move_up(fifo_element)
  if child.size > 0:
    fifo.append(child)

  child = make_move_down(fifo_element)
  if child.size > 0:
    fifo.append(child)

print " ***** explored :"
print explored.popleft()
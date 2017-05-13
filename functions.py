
import numpy
from numpy import reshape

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

def get_possible_actions(element_string ):
    # print " inside get_possible_actions " + element_string
    np_array_input = to_table(element_string)
    # print np_array_input
    zero_position = numpy.where(np_array_input == "0")
    # print zero_position
    # print " zero position !!!!!!  " + str(zero_position)
    zero_position_row = int(zero_position[0])
    zero_position_col = int(zero_position[1])
    # print type(zero_position_row)
    # print zero_position_col

    possible_actions = []
    if zero_position_row > 0:
        possible_actions.append("UP")

    if zero_position_row < 2:
        possible_actions.append("DOWN")

    if zero_position_col > 0:
        possible_actions.append("LEFT")


    if zero_position_col < 2:
        possible_actions.append("RIGHT")

    return possible_actions

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

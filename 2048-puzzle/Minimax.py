import numpy as np
import Helper
from sys import maxsize


def minimize(grid):
    minChild = None
    minUtility = maxsize

    for move in grid.getAvailableMoves():
            # print ' ***** move *******  ' + actionDic[m]
            grid_copy = grid.clone()
            grid_copy.move(move)
            (object, utility) = maximize(grid_copy)
            if utility < minUtility:
                min_child = grid_copy
                min_utility = move


    return (min_child, min_utility)

def maximize(grid):
    maxChild = None
    maxUtility = -maxsize

    for move in grid.getAvailableMoves():
            grid_copy = grid.clone()
            grid_copy.move(move)
            (object, utility) = minimize(grid_copy)
            if utility > maxUtility:
                max_child = grid_copy
                max_utility = move

    return (max_child, max_utility)

# def main():
#
#
# if __name__ == '__main__':
#     main()
#

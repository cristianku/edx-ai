# from random import randint
from BaseAI import BaseAI
import random


class ComputerAI(BaseAI):
    def getMove(self, grid):
        # random.seed(9001)

        cells = grid.getAvailableCells()

        return cells[random.randint(0, len(cells) - 1)] if cells else None

class board:
    def __init__(self, input_board_str):
        self.board = input_board_str

    def make_move(self, direction):
        zero_position = self.board.index("0")


    def possible_actions(self):
        zero_position = self.board.index("0")
        self.possible_actions = []
        if self.zero_position == 0:
            self.possible_actions.append("Down")
            self.possible_actions.append("Right")


        if self.zero_position == 1:
            self.possible_actions.append("Down")
            self.possible_actions.append("Left")
            self.possible_actions.append("Right"

        if self.zero_position == 2:
            self.possible_actions.append("Down")
            self.possible_actions.append("Left")

        if self.zero_position == 3:
            self.possible_actions.append("Up")
            self.possible_actions.append("Down")
            self.possible_actions.append("Right")

        if self.zero_position == 4:
            self.possible_actions.append("Up")
            self.possible_actions.append("Down")
            self.possible_actions.append("Left")
            self.possible_actions.append("Right")

        if self.zero_position == 5:
            self.possible_actions.append("Up")
            self.possible_actions.append("Down")
            self.possible_actions.append("Left")

            if self.zero_position == 5:



                self.possible_actions.append("Up")
self.possible_actions.append("Down")
self.possible_actions.append("Left")
self.possible_actions.append("Right")
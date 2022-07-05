# Author: Devon Miller
# Date: 5/31/2021
# Description: a class containing game rules and a game board. the board is 4X4 with 4 red pieces in the bottom row and 4 yellow pieces in the top row. pieces can move diagonally or non diagonally and must move until it is stopped by a piece or the boards edge. at the end ofa move pieces that are aligned non diagonally to the piece that was moved are flipped, the game is won when one player runs out of pieces or cannot make a move

class OrthokonBoard:
    """this class contains rules and records the board to a gave permitting diagonal and non diagonal movements flipping adjacent pieces after moves where a winner is had once no more moves can be made by the player"""
    
    def __init__(self):
        """initializing game state and current board as a list of 4 lists"""
        self._current_state = "UNFINISHED"
        self._current_board = [["red", "red", "red", "red"], [0, 0, 0, 0], [0, 0, 0, 0], ["yellow", "yellow", "yellow", "yellow"]]

    def get_current_state(self):
        """gets current game state"""
        return self._current_state

    def make_move(self, origional_row, origional_column, new_row, new_column):
        """takes new move from old place on board, contains rules and updates winner and board"""
        
        count = 0
        if new_row != origional_row and new_column != origional_column and abs(new_row - origional_row) != abs(new_column - origional_column):
            return False                # the new ensures the attempted move is diagonal or orthokonel from the origional space
        if (origional_row, origional_column) == (new_row, new_column):
            return False                # makes sure new and old values arent equal
        if origional_row > 3 or origional_column > 3 or new_row > 3 or new_column > 3:
            return False                # move attempted must be in range
        if self._current_board[new_row][new_column] != 0:
            return False                # new space moved to must be unoccupied
        if self._current_state != "UNFINISHED":
            return False                # game must be unfinished for move to count
        # the following 40 lines check to make sure a piece couldnt have moved further in its direction without hitting the edge of the board or another piece each group of two if statements checks a certain direction and returns false if the piece couldve moved further
        if new_row == origional_row and new_column > origional_column and new_column <= 1:
            if self._current_board[new_row][new_column + 1] == 0 and self._current_board[new_row][new_column + 2] == 0:
                return False                          # checking the two spaces right after moving right
        if new_row == origional_row and new_column > origional_column and new_column <= 2:
            if self._current_board[new_row][new_column + 1] == 0:
                return False                          # checking the space right after moving right
        if origional_column == new_column and new_row > origional_row and new_row <= 1:
            if self._current_board[new_row+1][new_column] == 0 and self._current_board[new_row +2][new_column] == 0:
                return False                          # checking 2 spaces above after moving up
        if origional_column == new_column and new_row > origional_row and new_row <= 2:
            if self._current_board[new_row + 1][new_column] == 0:
                return False                          # checking space above
        if new_row == origional_row and new_column < origional_column and new_column >= 2:
            if self._current_board[new_row][new_column -1] == 0 and self._current_board[new_row][new_column -2] == 0:
                return False                          # checking 2 spaces to the left
        if new_row == origional_row and new_column < origional_column and new_column >= 1:
            if self._current_board[new_row][new_column - 1] == 0:
                return False                          # checking space to the left
        if new_row < origional_row and new_column == origional_column and new_row >= 2:
            if self._current_board[new_row -1][new_column] == 0 and self._current_board[new_row -2][new_column] ==0:
                return False                          # checking 2 spaces below
        if new_row < origional_row and new_column == origional_column and new_row >= 1:
            if self._current_board[new_row - 1][new_column] == 0:
                return False                        # checking space below
        if new_row > origional_row and new_column > origional_column and new_row <= 1 and new_column <= 1:
            if self._current_board[new_row + 1][new_column +1] == 0 and self._current_board[new_row + 2][new_column +2] ==0:
                return False                        # checking 2 spaces diagonal up right
        if new_row > origional_row and new_column > origional_column and new_row <= 2 and new_column <= 2:
            if self._current_board[new_row + 1][new_column + 1] == 0:
                return False                   # checking space diagonal up right
        if new_row > origional_row and new_column < origional_column and new_row <= 1 and new_column >= 2:
            if self._current_board[new_row +1][new_column -1] == 0 and self._current_board[new_row + 2][new_column -2] == 0:
                return False                      # checking 2 spaces diagonal up left
        if new_row > origional_row and new_column < origional_column and new_row <= 2 and new_column >= 1:
            if self._current_board[new_row + 1][new_column - 1] == 0:
                return False                     # checks diagonal up left
        if new_row < origional_row and new_column > origional_column and new_row >= 2 and new_column <= 1:
            if self._current_board[new_row - 1][new_column + 1] == 0 and self._current_board[new_row - 2][new_column +2] == 0:
                return False                      # checks 2 spaces diagonal down right
        if new_row < origional_row and new_column > origional_column and new_row >= 1 and new_column <= 2:
            if self._current_board[new_row - 1][new_column + 1] == 0:
                return False                       # checks the space diagonal down right
        if new_row < origional_row and new_column < origional_column and new_row >= 2 and new_column >= 2:
            if self._current_board[new_row - 1][new_column - 1] == 0 and self._current_board[new_row - 2][new_column -2] == 0:
                return False                      # checks the two spaces diagonal down left
        if new_row < origional_row and new_column < origional_column and new_row >= 1 and new_column >= 1:
            if self._current_board[new_row - 1][new_column - 1] == 0:
                return False                      # checks the space diagonal down left
        else:
            if self._current_board[origional_row][origional_column] == "red":  # run this part for "red" moves
                if new_column <= 2:                                 # makes sure potential changes are to spaces within range
                    if self._current_board[new_row][new_column + 1] == "yellow":
                        self._current_board[new_row][new_column + 1] = "red" # if piece to the right is yellow it becomes red
                if new_column >= 1:                                     # makes sure potential changes are withing the board range
                    if self._current_board[new_row][new_column - 1] == "yellow":
                        self._current_board[new_row][new_column - 1] = "red"    # if piece to the left was yellow its now red
                if new_row >= 1:                                        # making sure changes are within range
                    if self._current_board[new_row - 1][new_column] == "yellow":
                        self._current_board[new_row - 1][new_column] = "red"  # if piece below was yellow its now red
                if new_row <= 2:
                    if self._current_board[new_row + 1][new_column] == "yellow":
                        self._current_board[new_row + 1][new_column] = "red"            # if space above was yellow its now red
                self._current_board[new_row][new_column] = self._current_board[origional_row][origional_column] # updates new value
                self._current_board[origional_row][origional_column] = 0                # sets origional value to zero
                if "yellow" not in self._current_board[0]:              # checking for "yellow" in first list within the list
                    if "yellow" not in self._current_board[1]:          # checking for "yellow" in second list in the list
                        if "yellow" not in self._current_board[2]:
                            if "yellow" not in self._current_board[3]:
                                self._current_state = "RED_WON"     # if "yellow" isnt in any list within the list the red wins
                # if a player has one piece and is surrounded they cannot make a move and lose the next 10 lines check whether there is a move to be made
                for num_yellows in self._current_board[0]:
                    if num_yellows == "yellow":
                        count += 1                  # if yellow is in the first list i the list count adds 1 for each yellow
                for num_yellows in self._current_board[1]:
                    if num_yellows == "yellow":
                        count += 1                  # if yellow is in second list in the current_board list add 1 for each yellow
                for num_yellows in self._current_board[2]:
                        if num_yellows == "yellow":
                            count += 1
                for num_yellows in self._current_board[3]:
                        if num_yellows == "yellow":
                            count += 1
                if count == 1:                       # the next part runs if there is exactly 1 yellow left
                    if self._current_board[0][0] == "yellow":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[0][1] == "red":
                            self._current_state = "RED_WON"         # if yellow surrounded in space 0, 0 red wins
                    if self._current_board[0][1] == "yellow":
                        if self._current_board[0][0] and self._current_board[1][0] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[0][2] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 0, 1 red wins
                    if self._current_board[0][2] == "yellow":
                        if self._current_board[0][1] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[1][3] and self._current_board[0][3] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 0, 2 red wins
                    if self._current_board[1][0] == "yellow":
                        if self._current_board[2][0] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1] and self._current_board[0][0] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 1, 0
                    if self._current_board[0][2] == "yellow":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[2][1] and self._current_board[3][1] and self._current_board[3][0] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 0, 2 red wins
                    if self._current_board[3][1] == "yellow":
                        if self._current_board[3][0] and self._current_board[2][1] and self._current_board[2][0] and self._current_board[2][2] and self._current_board[3][2] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 3, 1 red wins
                    if self._current_board[3][2] == "yellow":
                        if self._current_board[3][1] and self._current_board[2][1] and self._current_board[2][2] and self._current_board[2][3] and self._current_board[3][3] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 3, 2 red wins
                    if self._current_board[1][3] == "yellow":
                        if self._current_board[0][3] and self._current_board[0][2] and self._current_board[1][2] and self._current_board[2][2] and self._current_board[2][3] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 1, 3 red wins
                    if self._current_board[2][3] == "yellow":
                        if self._current_board[3][3] and self._current_board[3][2] and self._current_board[2][2] and self._current_board[1][2] and self._current_board[1][3] == "red":
                            self._current_state = "RED_WON"  # if yellow surrounded in space 2, 3 red wins
                    if self._current_board[3][0] == "yellow":
                        if self._current_board[3][1] and self._current_board[2][1] and self._current_board[2][0] == "red":
                            self._current_state = "RED_WON"        # if yellow surrounded in upper left corner red wins
                    if self._current_board[0][3] == "yellow":
                        if self._current_board[1][3] and self._current_board[0][2] and self._current_board[1][2] == "red":
                            self._current_state = "RED_WON"        # if yellow surrounded in bottom right corner red wins
                    if self._current_board[3][3] == "yellow":
                        if self._current_board[3][2] and self._current_board[2][2] and self._current_board[2][3] == "red":
                            self._current_state = "RED_WON"        # if yellow surrounded in upper right corner red wins
                if count == 2:                       #if yellow has 2 pieces left this portion of code runs
                    if self._current_board[0][0] and self._current_board[0][1] == "yellow":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[2][0] == "red":
                            self._current_state = "RED_WON"              # if yellow is surrounded in places 0, 0 and 1, 0 red wins
                    if self._current_board[0][0] and self._current_board[1][0] == "yellow":
                        if self._current_board[2][0] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1] == "red":
                            self._current_state = "RED_WON"              # if yellow is surrounded in places 0, 0 and 1, 0 red wins
                    if self._current_board[3][0] and self._current_board[3][1] == "yellow":
                        if self._current_board[3][2] and self._current_board[2][2] and self._current_board[2][1] and self._current_board[2][0] == "red":
                            self._current_state = "RED_WON"              # yellow is in places 3, 0 and 3, 1 and is surrounded
                    if self._current_board[3][0] and self._current_board[2][0] == "yellow":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[2][1] and self._current_board[3][1] == "red":
                            self._current_state = "RED_WON"              # yellow is surrounded in places 3, 0 and 2, 0
                    if self._current_board[3][3] and self._current_board[2][3] == "yellow":
                        if self._current_board[1][3] and self._current_board[1][2] and self._current_board[2][2] and self._current_board[3][2] == "red":
                            self._current_state = "RED_WON"              # yellow is surrounded in spaces 3, 3 and 2 3
                    if self._current_board[3][3] and self._current_board[3][2] == "yellow":
                        if self._current_board[3][1] and self._current_board[2][1] and self._current_board[2][2] and self._current_board[2][3] == "red":
                            self._current_state = "RED_WON"              # yellow is surrounded from spaces 3, 3 and 3, 2
                    if self._current_board[0][3] and self._current_board[0][2] == "yellow":
                        if self._current_board[0][1] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[1][3] == "red":
                            self._current_state = "RED_WON"              # yellow is surrounded from spaces 0,3 and 0,2
                    if self._current_board[0][3] and self._current_board[1][3] == "yellow":
                        if self._current_board[0][2] and self._current_board[1][2] and self._current_board[2][2] and self._current_board[2][3] == "red":
                            self._current_state = "RED_WON"              # yellow is surrounded from spaces 0, 3 and 1, 3
                    if self._current_board[0][1] and self._current_board[0][2] == "yellow":
                        if self._current_board[1] and self._current_board[0][0] and self._current_board[0][3] == "red":
                            self._current_state = "RED_WON"             # yellow is surrounded on the bottom row center spots
                    if self._current_board[3][1] and self._current_board[3][2] == "yellow":
                        if self._current_board[2] and self._current_board[3][0] and self._current_board[3][3] == "red":
                            self._current_state = "RED_WON"             # yellow is surrounded on the top center spots
                    if self._current_board[1][0] and self._current_board[2][0] == "yellow":
                        if self._current_board[0][0] and self._current_board[3][0] and self._current_board[3][1] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1]== "red":
                            self._current_state = "RED_WON"         # yellow surrounded on left middle spaces
                    if self._current_board[1][3] and self._current_board[2][3] == "yellow":
                        if self._current_board[3][3] and self._current_board[0][3] and self._current_board[3][2] and self._current_board[2][2] and self._current_board[1][2] and self._current_board[0][2] == "red":
                            self._current_state = "RED_WON"  # yellow surrounded on right middle spaces
                return True

            if self._current_board[origional_row][origional_column] == "yellow":        # this portion runs if yellow is being moved
                if new_column <= 2:                               # ensuring move to be made is in range
                    if self._current_board[new_row][new_column + 1] == "red":
                        self._current_board[new_row][new_column + 1] = "yellow"     # if space to right was red its now yellow
                if new_column >= 1:                             # ensuring move to be made is in range
                    if self._current_board[new_row][new_column - 1] == "red":
                        self._current_board[new_row][new_column - 1] = "yellow"     # if space left was red its now yellow
                if new_row >= 1:
                    if self._current_board[new_row - 1][new_column] == "red":
                        self._current_board[new_row - 1][new_column] = "yellow"     # if space below was red its now yellow
                if new_row <= 2:
                    if self._current_board[new_row + 1][new_column] == "red":
                        self._current_board[new_row + 1][new_column] = "yellow"     # if space above was red its now yellow
                self._current_board[new_row][new_column] = self._current_board[origional_row][origional_column]  # setting new space to yellow
                self._current_board[origional_row][origional_column] = 0        # sets origional space to zero
                if "red" not in self._current_board[0]:
                    if "red" not in self._current_board[1]:
                        if "red" not in self._current_board[2]:
                            if "red" not in self._current_board[3]:         # checks for red in all lists in current_board
                                self._current_state = "YELLOW_WON"          # if no spaces are red yellow wins
                for num_reds in self._current_board[0]:   # checking for red in first list in current_board
                    if num_reds == "red":
                        count += 1                      # for each red in that list add 1
                for num_reds in self._current_board[1]:     # checks for red in second list
                    if num_reds == "red":
                        count += 1                      # for each red in list add 1
                for num_reds in self._current_board[2]:
                    if num_reds == "red":
                        count += 1
                for num_reds in self._current_board[3]:
                    if num_reds == "red":
                        count += 1
                if count == 1:                  # this portion runs if there is only 1 red left and checks if a move an be made
                    if self._current_board[0][0] == "red":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[0][1] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red in lower left corner is surrounded yellow wins
                    if self._current_board[0][1] == "red":
                        if self._current_board[0][0] and self._current_board[1][0] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[0][2] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red is surrounded in space 0, 1 yellow wins
                    if self._current_board[0][2] == "red":
                        if self._current_board[0][1] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[1][3] and self._current_board[0][3] == "yellow":
                            self._current_state = "YELLOW_WON"         # if red is surrounded in space 0, 1 yellow wins
                    if self._current_board[1][0] == "red":
                        if self._current_board[2][0] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1] and self._current_board[0][0] == "yellow":
                            self._current_state = "YELLOW_WON"        # if red is surrounded in space 1, 0 yellow wins
                    if self._current_board[2][0] == "red":
                        if self._current_board[3][0] and self._current_board[3][1] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[1][0] == "yellow":
                            self._current_state = "YELLOW_WON"        # if red is surrounded in space 2, 0 yellow wins
                    if self._current_board[3][0] == "red":
                        if self._current_board[3][0] and self._current_board[2][1] and self._current_board[3][1] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red upper left corner surrounded yellow wins
                    if self._current_board[3][1] == "red":
                        if self._current_board[3][2] and self._current_board[2][2] and self._current_board[2][1] and self._current_board[2][0] and self._current_board[3][0] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red is surrounded at space 3, 1 yellow wins
                    if self._current_board[3][2] == "red":
                        if self._current_board[3][3] and self._current_board[2][3] and self._current_board[2][2] and self._current_board[2][1] and self._current_board[3][1] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red is surrounded in space 3, 2 yellow wins
                    if self._current_board[0][3] == "red":
                        if self._current_board[0][3] and self._current_board[0][2] and self._current_board[1][2] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red in lower right space surrounded yellow wins
                    if self._current_board[2][3] == "red":
                        if self._current_board[3][3] and self._current_board[3][2] and self._current_board[2][2] and self._current_board[1][1] and self._current_board[1][3] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red is surrounded in spot 2, 3 yellow wins
                    if self._current_board[1][3] == "red":
                        if self._current_board[2][3] and self._current_board[2][2] and self._current_board[1][2] and self._current_board[0][2] and self._current_board[0][3] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red is surrounded at space 2, 3 yellow wins
                    if self._current_board[3][3] == "red":
                        if self._current_board[3][3] and self._current_board[2][2] and self._current_board[2][3] == "yellow":
                            self._current_state = "YELLOW_WON"      # if red in upper right is surrounded yellow wins
                if count == 2:              #if red has 2 pieces left this portion of code runs
                    if self._current_board[0][0] and self._current_board[0][1] == "red":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[2][0] == "yellow":
                            self._current_state = "YELLOW_WON"              # if red is surrounded in places 0, 0 and 1, 0 yellow wins
                    if self._current_board[0][0] and self._current_board[1][0] == "red":
                        if self._current_board[2][0] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1] == "yellow":
                            self._current_state = "YELLOW_WON"              # if red is surrounded in places 0, 0 and 1, 0 yellow wins
                    if self._current_board[3][0] and self._current_board[3][1] == "red":
                        if self._current_board[3][2] and self._current_board[2][2] and self._current_board[2][1] and self._current_board[2][0] == "yellow":
                            self._current_state = "YELLOW_WON"              # red is in places 3, 0 and 3, 1 and is surrounded
                    if self._current_board[3][0] and self._current_board[2][0] == "red":
                        if self._current_board[1][0] and self._current_board[1][1] and self._current_board[2][1] and self._current_board[3][1] == "yellow":
                            self._current_state = "YELLOW_WON"              # red is surrounded in places 3, 0 and 2, 0
                    if self._current_board[3][3] and self._current_board[2][3] == "red":
                        if self._current_board[1][3] and self._current_board[1][2] and self._current_board[2][2] and self._current_board[3][2] == "yellow":
                            self._current_state = "YELLOW_WON"              # red is surrounded in spaces 3, 3 and 2 3
                    if self._current_board[3][3] and self._current_board[3][2] == "red":
                        if self._current_board[3][1] and self._current_board[2][1] and self._current_board[2][2] and self._current_board[2][3] == "yellow":
                            self._current_state = "YELLOW_WON"              # red is surrounded from spaces 3, 3 and 3, 2
                    if self._current_board[0][3] and self._current_board[0][2] == "red":
                        if self._current_board[0][1] and self._current_board[1][1] and self._current_board[1][2] and self._current_board[1][3] == "yellow":
                            self._current_state = "YELLOW_WON"              # red is surrounded from spaces 0,3 and 0,2
                    if self._current_board[0][3] and self._current_board[1][3] == "red":
                        if self._current_board[0][2] and self._current_board[1][2] and self._current_board[2][2] and self._current_board[2][3] == "yellow":
                            self._current_state = "YELLOW_WON"
                    if self._current_board[0][1] and self._current_board[0][2] == "red":
                        if self._current_board[1] and self._current_board[0][0] and self._current_board[0][3] == "yellow":
                            self._current_state = "YELLOW_WON"             # red is surrounded on the bottom row center spots
                    if self._current_board[3][1] and self._current_board[3][2] == "red":
                        if self._current_board[2] and self._current_board[3][0] and self._current_board[3][3] == "yellow":
                            self._current_state = "YELLOW_WON"             # red is surrounded on the top center spots
                    if self._current_board[1][0] and self._current_board[2][0] == "red":
                        if self._current_board[0][0] and self._current_board[3][0] and self._current_board[3][1] and self._current_board[2][1] and self._current_board[1][1] and self._current_board[0][1]== "yellow":
                            self._current_state = "YELLOW_WON"         # red surrounded on left middle spaces
                    if self._current_board[1][3] and self._current_board[2][3] == "red":
                        if self._current_board[3][3] and self._current_board[0][3] and self._current_board[3][2] and self._current_board[2][2] and self._current_board[1][2] and self._current_board[0][2] == "yellow":
                            self._current_state = "YELLOW_WON"  # red surrounded on right middle spaces
                return True



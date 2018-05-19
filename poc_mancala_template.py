"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

# Import GUI code once you feel your code is correct
from utilities import poc_mancala_gui


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board = list()
        self.board.append(0)

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board = list(configuration)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        arr = list()
        for i in range(0, len(self.board)):
            arr.append(self.board[len(self.board) - i - 1])
        return str(arr)


    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for i in range(1,len(self.board)):
            if self.board[i] != 0:
                return False

        return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return house_num == self.board[house_num] and house_num != 0

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num) and house_num != 0:
            for i in range(0, house_num):
                self.board[i] = self.board[i] + 1
            self.board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """

        for i in range(1, len(self.board)):
            if self.is_legal_move(i):
                return i

        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
		After each move, move the seeds in the house closest to the store
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        original_board = list(self.board)
        moves = list()

        # i = 99999
        i = self.choose_move()
        while True:

            if i == 0:
                break
            else:
                moves.append(i)
                self.apply_move(i)
                i = self.choose_move()

        self.board = list(original_board)
        return moves


poc_mancala_gui.run_gui(SolitaireMancala())

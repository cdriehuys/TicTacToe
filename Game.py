__author__ = 'Chathan Driehuys'

class Board:

    def __init__(self):
        """
        Initializes the Board class.
        """

        # create empty board
        self.board = []

        # initialize the board to be empty
        for i in range(3):

            row = []

            for j in range(3):
                row.append(None)

            self.board.append(row)

    def __str__(self):
        """
        Create a string representation of the board.
        :return: A string representation of the board.
        :rtype: str
        """
        ret_str = ""
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(0, 0), self.print_square(0, 1), self.print_square(0, 2))
        ret_str += "   |   |   \n"
        ret_str += "---+---+---\n"
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(1, 0), self.print_square(1, 1), self.print_square(1, 2))
        ret_str += "   |   |   \n"
        ret_str += "---+---+---\n"
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(2, 0), self.print_square(2, 1), self.print_square(2, 2))
        ret_str += "   |   |   \n\n"

        return ret_str

    def print_square(self, row, col):
        """
        Returns the character at the given square. If the given square is empty, a space (" ") is returned.
        :param row: The row of the square.
        :type row: int
        :param col: The column of the square.
        :type col: int
        :return: The character in the specified square.
        :rtype: str
        """
        return str(self.get_square(row, col))

    def get_square(self, row, col):
        """
        Get the game piece at the specified location.
        :param row: The row index of the square.
        :type row: int
        :param col: The column index of the square.
        :type col: int
        :return: The game piece in the square.
        :rtype: str
        """
        return self.board[row][col] if self.board[row][col] else " "

    def place_piece(self, row, col, piece):
        """
        Places the given piece at the given location.
        :param row: The row index to place the piece at.
        :type row: int
        :param col: The column index to place the piece at.
        :type col: int
        :param piece: The piece to place.
        :type piece: str
        :return:
        :rtype:
        """
        self.board[row][col] = piece


class Game:

    def __init__(self, player1, player2):
        """
        Initialize the game.
        """
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

board = Board()
print(board)
board.place_piece(1, 1, 'X')
print(board)
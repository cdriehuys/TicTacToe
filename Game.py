__author__ = 'Chathan Driehuys'

class Board:

    def __init__(self):
        """
        Initializes the Board class.
        """

        # create empty board
        self.squares = []

        # initialize the board to be empty
        for i in range(9):
            self.squares.append(None)

    def __str__(self):
        """
        Create a string representation of the board.
        :return: A string representation of the board.
        :rtype: str
        """
        ret_str = ""
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(7), self.print_square(8), self.print_square(9))
        ret_str += "   |   |   \n"
        ret_str += "---+---+---\n"
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(4), self.print_square(5), self.print_square(6))
        ret_str += "   |   |   \n"
        ret_str += "---+---+---\n"
        ret_str += "   |   |   \n"
        ret_str += " %s | %s | %s \n" % (self.print_square(1), self.print_square(2), self.print_square(3))
        ret_str += "   |   |   \n\n"

        return ret_str

    def print_square(self, num):
        """
        Returns the character at the given square. If the given square is empty, a space (" ") is returned.
        :param row: The row of the square.
        :type row: int
        :param col: The column of the square.
        :type col: int
        :return: The character in the specified square.
        :rtype: str
        """
        return str(self.get_square(num))

    def get_square(self, num):
        """
        Get a square by number based on this chart:

           |   |
         7 | 8 | 9
           |   |
        ---+---+---
           |   |
         4 | 5 | 6
           |   |
        ---+---+---
           |   |
         1 | 2 | 3
           |   |

        :param num: The square number to get.
        :type num: int
        :return: The piece at the specified square.
        :rtype: str
        """
        return self.squares[num - 1] if self.squares[num - 1] else " "

    def place_piece(self, num, piece):
        """
        Places the given piece at the given location.
        :param num: The square number to place the piece in.
        :type num: int
        :param piece: The piece to place.
        :type piece: str
        :return:
        :rtype:
        """
        self.squares[num - 1] = piece


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
board.place_piece(5, 'X')
print(board)
board.get_square(5)


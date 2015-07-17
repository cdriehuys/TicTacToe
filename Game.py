__author__ = 'Chathan Driehuys'

import random


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

    def squares_equal(self, square_nums):
        """
        Test if all the square numbers given have the same (not None) value.
        :param square_nums: A list of square numbers to check.
        :type square_nums: tuple
        :return: If the squares all contain the same not None value.
        :rtype: bool
        """
        if len(square_nums) < 1:
            return True

        token = self.get_square(square_nums[0])

        if token == " ":
            return False

        for i in range(1, len(square_nums)):
            if self.get_square(square_nums[i]) != token:
                return False

        return True

    def get_possible_moves(self):
        """
        Returns a list of possible move locations.
        :return:
        :rtype:
        """
        moves = []

        for i in range(len(self.squares)):
            if not self.squares[i]:
                moves.append(i + 1)

        return moves


class Game:

    WINNING_COMBOS = (
        # Horizontal wins
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),

        # Vertical wins
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),

        # Diagonal wins
        (1, 5, 9),
        (3, 5, 7)
    )

    def __init__(self, player1, player2):
        """
        Initialize the game.
        """
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def game_won(self):
        """
        Determine if the game has been won yet.
        :return:
        :rtype:
        """
        for combo in Game.WINNING_COMBOS:
            if self.board.squares_equal(combo):
                return True

        return False

    def play(self):
        """
        Plays the game.
        :return:
        :rtype:
        """
        while not self.game_won() and self.board.get_possible_moves():
            self.player1.play(self.board)
            print(self.board)
            if not self.game_won():
                self.player2.play(self.board)
                print(self.board)


class Player:
    def __init__(self, piece):
        """
        Initialize the player with a piece.
        :param piece: The player's game piece. Ex: 'X'
        :type piece: str
        :return:
        :rtype:
        """
        self.piece = piece

    def play(self, board):
        """
        Play a move on the given board.
        :param board:
        :type board:
        :return:
        :rtype:
        """
        pass


class DumbAI(Player):
    def play(self, board):
        """
        Play a random move.
        :param board:
        :type board:
        :return:
        :rtype:
        """
        moves = board.get_possible_moves()
        board.place_piece(moves[random.randint(0, len(moves) - 1)], self.piece)

class HumanPlayer(Player):
    def play(self, board):
        """
        Ask for a move from the player and try to make that move.
        :param board:
        :type board:
        :return:
        :rtype:
        """
        possible = board.get_possible_moves()
        valid = False
        while not valid:
            move = input("Which square would you like to place your piece in?: ")
            try:
                move = int(move)
                if move in possible:
                    valid = True
                else:
                    print("That move has already been made, or is out of range.")
            except ValueError:
                print("Please enter a valid integer.")

        board.place_piece(move, self.piece)


if __name__ == "__main__":
    game = Game(HumanPlayer('X'), DumbAI('O'))
    game.play()


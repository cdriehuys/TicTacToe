__author__ = 'Chathan Driehuys'

import random


class Board:

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

    def __init__(self):
        """
        Initializes the Board class.
        """

        # create empty board
        self.squares = []

        # initialize the board to be empty
        for i in range(9):
            self.squares.append(None)

        self.winner_piece = None

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
        return str(self.get_square(num)) if self.get_square(num) else ' '

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
        return self.squares[num - 1]

    def set_square(self, num, piece):
        """
        Places the given piece at the given location.
        :param num: The square number to place the piece in.
        :type num: int
        :param piece: The piece to place.
        :type piece: str
        """
        self.squares[num - 1] = piece

    def squares_equal(self, square_nums):
        """
        Test if all the square numbers given have the same (not None) value.
        :param square_nums: A list of square numbers to check.
        :type square_nums: tuple
        :return: True if the squares all contain the same not None value, False otherwise.
        :rtype: bool
        """
        if len(square_nums) < 1:
            return True

        token = self.get_square(square_nums[0])

        if not token:
            return False

        for i in range(1, len(square_nums)):
            if self.get_square(square_nums[i]) != token:
                return False

        return True

    def get_possible_moves(self):
        """
        Returns a list of possible move locations.
        :return: A list of possible squares to make a move in.
        :rtype: list
        """
        moves = []

        for i in range(len(self.squares)):
            if not self.squares[i]:
                moves.append(i + 1)

        return moves

    def copy(self):
        """
        Returns a new board that is a copy of this one.
        :return: A copy of this board.
        :rtype: Board
        """
        new_board = Board()
        new_board.squares = self.squares.copy()
        return new_board

    def game_won(self):
        """
        Determine if the game has been won yet.
        :return:
        :rtype:
        """
        for combo in Board.WINNING_COMBOS:
            if self.squares_equal(combo):
                self.winner_piece = self.get_square(combo[0])
                return True

        return False


class Game:
    def __init__(self, player1, player2):
        """
        Initialize the game.
        :param player1: The class of the first player.
        :param player2: The class of the second player.
        """
        self.board = Board()

        self.player1 = player1(self, 'X')
        self.player2 = player2(self, 'O')

        self.player_piece_dict = {
            'X': self.player1,
            'O': self.player2,
        }

        self.player1_turn = True

    def play(self):
        """
        Plays the game.
        """
        while not self.board.game_won() and self.board.get_possible_moves():

            if self.player1_turn:
                self.player1.play()
            else:
                self.player2.play()

            print(self.board)
            self.player1_turn = not self.player1_turn

    def make_move(self, player, position):
        """
        Makes a move in a safe manner by checking if the square that the move is made in already has a piece.
        :param player: The player making the move.
        :type player: Player
        :param position: The square to make the move in.
        :type position: int
        :return:
        :rtype:
        """
        if self.board.get_square(position):
            raise RuntimeError("That square is already occupied.")

        self.board.set_square(position, player.piece)

    def get_by_piece(self, piece):
        """
        Return a player based on their piece.
        :return: The player with the given piece.
        :rtype: Player
        """
        return self.player_piece_dict.get(piece, None)

    def get_winner(self):
        """
        Returns the winner of the game.
        :return: The winner of the game.
        :rtype: Player
        """
        return self.get_by_piece(self.board.winner_piece)


class Player:
    def __init__(self, game, piece):
        """
        Initialize the player with a piece.
        :param game: The game the player belongs to.
        :type game: Game
        :param piece: The player's game piece. Ex: 'X'
        :type piece: str
        """
        self.game = game
        self.piece = piece

        self.board = self.game.board

    def play(self):
        """
        Play a move on the given board.
        """
        self.board = self.game.board


class HumanPlayer(Player):
    def play(self):
        """
        Ask for a move from the player and try to make that move.
        """
        super(HumanPlayer, self).play()

        move = -1

        possible = self.board.get_possible_moves()
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

        self.game.make_move(self, move)


class DumbAI(Player):
    def play(self):
        """
        Play a random move.
        """
        super(DumbAI, self).play()

        moves = self.board.get_possible_moves()
        self.board.set_square(moves[random.randint(0, len(moves) - 1)], self.piece)


class DefinedMovesAI(Player):
    """
    An AI that pays no attention to the player. It just selects the first available move from a list of best possible\
    moves.
    """
    # the best moves to make, in order of preference
    BEST_MOVES = (5, 1, 3, 9, 2, 4, 6, 8)

    def play(self):
        """
        Selects the best available move.
        """
        super(DefinedMovesAI, self).play()

        possible = self.board.get_possible_moves()
        for move in DefinedMovesAI.BEST_MOVES:
            if move in possible:
                self.board.set_square(move, self.piece)
                break


class SmartDefinedMovesAI(Player):
    """
    An improved version of the DefinedMovesAI that looks ahead one move. If it can win in the next move, it will take
    that move. If it can't win, it looks to see if the player can win in their next turn, and if they can, it blocks
    that move. If neither of those conditions are true, it will pull the next move from the list of best moves.
    """
    # the best moves to make, in order of preference
    BEST_MOVES = (5, 1, 3, 9, 2, 4, 6, 8)

    def play(self):
        """
        Tries to win, then tries to block the player, then selects the next best move.
        """
        super(SmartDefinedMovesAI, self).play()

        possible = self.board.get_possible_moves()

        for move in possible:
            temp_board = self.board.copy()

            temp_board.set_square(move, self.piece)

            if temp_board.game_won():
                self.board.set_square(move, self.piece)
                return

        for move in possible:
            temp_board = self.board.copy()

            # TODO: Find better way to get the other piece to allow for arbitrary tokens, not just 'X' and 'O'
            temp_board.set_square(move, 'O' if self.piece == 'X' else 'X')

            if temp_board.game_won():
                self.board.set_square(move, self.piece)
                return

        for move in SmartDefinedMovesAI.BEST_MOVES:
            if move in possible:
                self.board.set_square(move, self.piece)
                return


class PerfectAI(Player):
    """
    This AI player utilizes a minimax search to find the optimal move.
    """
    def minimax(self, is_players_turn, board, level=0):
        """
        Finds the best move using a minimax algorithm
        :param is_players_turn: If it is the player's turn, in which case we would try to maximize the score.
        :type is_players_turn: bool
        :param board: The board we're working with.
        :type board: Board
        """
        best_score = -999 if is_players_turn else 999
        best_move = -1

        possible = board.get_possible_moves()

        if board.game_won():

            if board.winner_piece == self.piece:
                best_score = 100
            elif board.winner_piece:
                best_score = -100

        elif not possible:
            best_score = 0

        else:
            if is_players_turn:
                for move in possible:
                    temp_board = board.copy()
                    temp_board.set_square(move, self.piece)
                    score, m = self.minimax(False, temp_board, level=(level + 1))
                    if score > best_score:
                        best_score = score - level
                        best_move = move

            else:
                for move in possible:
                    temp_board = board.copy()
                    temp_board.set_square(move, 'O' if self.piece == 'X' else 'X')
                    score, m = self.minimax(True, temp_board, level=(level + 1))
                    if score < best_score:
                        best_score = score + level
                        best_move = move

        return best_score, best_move

    def play(self):
        """
        Plays a move.
        """
        super(PerfectAI, self).play()

        score, move = self.minimax(True, self.board)
        self.game.make_move(self, move)


def print_headline(text):
    """
    Prints text in a noticeable manner.
    :param text: The text to print.
    :type text: str
    """
    print('#' * 80)
    print('# %s' % text, end='')
    print(' ' * (80 - len(text) - 4), end='')
    print(' #')
    print('#' * 80)


if __name__ == "__main__":
    tic_tac_toe = Game(HumanPlayer, PerfectAI)
    tic_tac_toe.play()

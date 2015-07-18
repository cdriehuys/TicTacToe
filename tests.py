__author__ = 'Chathan'

from unittest import TestCase

from Game import Board, Game, Player


class BoardTest(TestCase):
    def test_init(self):
        """
        The board's init method should create an array with 9 None values.
        :return:
        :rtype:
        """
        board = Board()
        test_list = [None] * 9
        self.assertEqual(test_list, board.squares)

    def test_get_index_values(self):
        """
        Squares should be fetched using a pattern like a num-pad on a keyboard. The bottom-left square should be square
        '1', and the top-right square should be square '9'.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(3, 'X')
        self.assertEqual(board.squares[2], board.get_square(3))

    def test_get_emtpy_square(self):
        """
        Trying to get an empty square should return None.
        :return:
        :rtype:
        """
        board = Board()
        self.assertEqual(None, board.get_square(1))

    def test_get_filled_square(self):
        """
        Getting a filled square should return a string of that piece. (For now, might change to using a separate class
        for pieces later on.)
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(1, 'X')
        self.assertEqual('X', board.get_square(1))

    def test_print_empty_square(self):
        """
        Printing an empty square should result in ' '.
        :return:
        :rtype:
        """
        board = Board()
        self.assertEqual(' ', board.print_square(1))

    def test_print_filled_square(self):
        """
        Printing a square with a piece in it should result in that piece ('X' or 'O').
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(1, 'X')
        self.assertEqual('X', board.print_square(1))

    def test_set_square(self):
        """
        Placing a piece should set that square to the specified piece.
        :return:
        :rtype:
        """
        board = Board()
        self.assertEqual(None, board.get_square(5))
        board.set_square(5, 'X')
        self.assertEqual('X', board.get_square(5))

    def test_squares_equal_with_blank_list(self):
        """
        Trying to call 'squares_equal' with a blank list or tuple should return true.
        :return:
        :rtype:
        """
        board = Board()
        self.assertTrue(board.squares_equal(()))

    def test_squares_equal_with_blank_squares(self):
        """
        If any squares are 'None', the function should return false, even if all the squares given are the same.
        :return:
        :rtype:
        """
        board = Board()
        self.assertFalse(board.squares_equal((1, 2, 3)))

    def test_squares_equal_with_different_squares(self):
        """
        If the squares aren't the same, the function should return false.
        """
        board = Board()
        board.set_square(1, 'X')
        board.set_square(2, 'O')
        board.set_square(3, 'X')
        self.assertFalse(board.squares_equal((1, 2, 3)))

    def test_squares_equal_with_same_squares(self):
        """
        If all the squares in the list have the same piece in them, the function should return true.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(1, 'X')
        board.set_square(2, 'X')
        board.set_square(3, 'X')
        self.assertTrue(board.squares_equal((1, 2, 3)))

    def test_possible_moves_with_empty_board(self):
        """
        Getting the possible moves from an empty board should return a list containing the numbers in the range [1, 9].
        :return:
        :rtype:
        """
        board = Board()
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            board.get_possible_moves()
        )

    def test_possible_moves_with_some_pieces(self):
        """
        Getting the possible moves from a board should return the square numbers that have no piece in them.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(2, 'X')
        board.set_square(6, 'O')
        board.set_square(8, 'X')
        board.set_square(4, 'O')
        self.assertListEqual(
            [1, 3, 5, 7, 9],
            board.get_possible_moves()
        )

    def test_game_won_with_no_win(self):
        """
        If the game has not been won by a player yet, the function should return false.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        self.assertFalse(board.game_won())

    def test_game_won_with_win(self):
        """
        If a player has 3 pieces in a line, the game should be won and the function should return true.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        board.set_square(8, 'X')
        board.set_square(1, 'O')
        board.set_square(4, 'X')
        board.set_square(2, 'O')
        self.assertTrue(board.game_won())


class GameTest(TestCase):
    def test_game_won_with_no_win(self):
        """
        If the game has not been won by a player yet, the function should return false.
        :return:
        :rtype:
        """
        board = Board()
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        self.assertFalse(board.game_won())

    def test_game_won_with_win(self):
        """
        If a player has 3 pieces in a line, the game should be won and the function should return true.
        :return:
        :rtype:
        """
        game = Game(Player, Player)
        board = game.board
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        board.set_square(8, 'X')
        board.set_square(1, 'O')
        board.set_square(4, 'X')
        board.set_square(2, 'O')
        self.assertTrue(board.game_won())


class PlayerTest(TestCase):
    def test_init(self):
        """
        After initialization, the player's piece should be set to the one it was called with.
        :return:
        :rtype:
        """
        game = Game(Player, Player)
        player = game.player1
        self.assertEqual('X', player.piece)

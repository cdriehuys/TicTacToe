__author__ = 'Chathan'

from unittest import TestCase

from Game import Board, Game


class BoardTest(TestCase):
    def test_init(self):
        """
        The board's init method should create an array with 9 None values.
        :return:
        :rtype:
        """
        board = Board()
        test_list = [None for i in range(9)]
        self.assertEqual(test_list, board.squares)

    def test_get_index_values(self):
        """
        Squares should be fetched using a pattern like a num-pad on a keyboard. The bottom-left square should be square
        '1', and the top-right square should be square '9'.
        :return:
        :rtype:
        """
        board = Board()
        board.place_piece(3, 'X')
        self.assertEqual(board.squares[2], board.get_square(3))

    def test_get_emtpy_square(self):
        """
        Trying to get an empty square should return ' '.
        :return:
        :rtype:
        """
        board = Board()
        self.assertEqual(' ', board.get_square(1))

    def test_get_filled_square(self):
        """
        Getting a filled square should return a string of that piece. (For now, might change to using a separate class
        for pieces later on.)
        :return:
        :rtype:
        """
        board = Board()
        board.place_piece(1, 'X')
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
        board.place_piece(1, 'X')
        self.assertEqual('X', board.print_square(1))

    def test_place_piece(self):
        """
        Placing a piece should set that square to the specified piece.
        :return:
        :rtype:
        """
        board = Board()
        self.assertEqual(' ', board.get_square(5))
        board.place_piece(5, 'X')
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

    def test_squares_equal_with_same_squares(self):
        """
        If all the squares in the list have the same piece in them, the function should return true.
        :return:
        :rtype:
        """
        board = Board()
        board.place_piece(1, 'X')
        board.place_piece(2, 'X')
        board.place_piece(3, 'X')
        self.assertTrue(board.squares_equal((1, 2, 3)))


class GameTest(TestCase):
    def test_game_won_with_no_win(self):
        """
        If the game has not been won by a player yet, the function should return false.
        :return:
        :rtype:
        """
        game = Game(None, None)
        board = game.board
        board.place_piece(7, 'O')
        board.place_piece(5, 'X')
        board.place_piece(3, 'O')
        self.assertFalse(game.game_won())

    def test_game_won_with_win(self):
        """
        If a player has 3 pieces in a line, the game should be won and the function should return true.
        :return:
        :rtype:
        """
        game = Game(None, None)
        board = game.board
        board.place_piece(7, 'O')
        board.place_piece(5, 'X')
        board.place_piece(3, 'O')
        board.place_piece(8, 'X')
        board.place_piece(1, 'O')
        board.place_piece(4, 'X')
        board.place_piece(2, 'O')
        self.assertTrue(game.game_won())
__author__ = 'Chathan'

import unittest
from unittest import TestCase

from Game import Board, Game, Player, HumanPlayer, DefinedMovesAI, SmartDefinedMovesAI, PerfectAI


class BoardTest(TestCase):
    def test_init(self):
        """
        The board's init method should create an array with 9 None values.
        """
        board = Board()
        test_list = [None] * 9
        self.assertEqual(test_list, board.squares)

    def test_get_index_values(self):
        """
        Squares should be fetched using a pattern like a num-pad on a keyboard. The bottom-left square should be square
        '1', and the top-right square should be square '9'.
        """
        board = Board()
        board.set_square(3, 'X')
        self.assertEqual(board.squares[2], board.get_square(3))

    def test_get_emtpy_square(self):
        """
        Trying to get an empty square should return None.
        """
        board = Board()
        self.assertEqual(None, board.get_square(1))

    def test_get_filled_square(self):
        """
        Getting a filled square should return a string of that piece. (For now, might change to using a separate class
        for pieces later on.)
        """
        board = Board()
        board.set_square(1, 'X')
        self.assertEqual('X', board.get_square(1))

    def test_print_empty_square(self):
        """
        Printing an empty square should result in ' '.
        """
        board = Board()
        self.assertEqual(' ', board.print_square(1))

    def test_print_filled_square(self):
        """
        Printing a square with a piece in it should result in that piece ('X' or 'O').
        """
        board = Board()
        board.set_square(1, 'X')
        self.assertEqual('X', board.print_square(1))

    def test_set_square(self):
        """
        Placing a piece should set that square to the specified piece.
        """
        board = Board()
        self.assertEqual(None, board.get_square(5))
        board.set_square(5, 'X')
        self.assertEqual('X', board.get_square(5))

    def test_squares_equal_with_blank_list(self):
        """
        Trying to call 'squares_equal' with a blank list or tuple should return true.
        """
        board = Board()
        self.assertTrue(board.squares_equal(()))

    def test_squares_equal_with_blank_squares(self):
        """
        If any squares are 'None', the function should return false, even if all the squares given are the same.
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
        """
        board = Board()
        board.set_square(1, 'X')
        board.set_square(2, 'X')
        board.set_square(3, 'X')
        self.assertTrue(board.squares_equal((1, 2, 3)))

    def test_possible_moves_with_empty_board(self):
        """
        Getting the possible moves from an empty board should return a list containing the numbers in the range [1, 9].
        """
        board = Board()
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            board.get_possible_moves()
        )

    def test_possible_moves_with_some_pieces(self):
        """
        Getting the possible moves from a board should return the square numbers that have no piece in them.
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

    def test_copy_with_blank_board(self):
        """
        Copying a blank board should create a new blank board. Modifying the squares on one should not change the
        squares on the other.
        """
        board = Board()
        new_board = board.copy()
        self.assertListEqual([None] * 9, new_board.squares)
        new_board.set_square(1, 'X')
        self.assertIsNone(board.get_square(1))
        self.assertEqual(new_board.get_square(1), 'X')

    def test_copy_with_filled_board(self):
        """
        Copying a board that has pieces in it should return an exact copy with all the same pieces.
        """
        board = Board()
        board.set_square(1, 'X')
        board.set_square(3, 'O')
        board.set_square(6, 'O')
        board.set_square(7, 'X')
        new_board = board.copy()
        self.assertListEqual(['X', None, 'O', None, None, 'O', 'X', None, None], new_board.squares)

    def test_game_won_with_no_win(self):
        """
        If the game has not been won by a player yet, the function should return false.
        """
        board = Board()
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        self.assertFalse(board.game_won())

    def test_game_won_with_win(self):
        """
        If a player has 3 pieces in a line, the game should be won and the function should return true. The board's
        winner_piece variable should also be set to the winner's piece.
        """
        board = Board()
        # make sure board's winner_piece variable is initially None
        self.assertIsNone(board.winner_piece)
        board.set_square(7, 'O')
        board.set_square(5, 'X')
        board.set_square(3, 'O')
        board.set_square(8, 'X')
        board.set_square(1, 'O')
        board.set_square(4, 'X')
        board.set_square(2, 'O')
        self.assertTrue(board.game_won())
        self.assertEqual('O', board.winner_piece)


class GameTest(TestCase):
    def test_game_init(self):
        """
        Make sure all the variables for the game class are set up correctly.
        """
        game = Game(Player, HumanPlayer)
        p1 = game.player1
        p2 = game.player2
        self.assertIsInstance(game.player1, Player)
        self.assertIsInstance(game.player2, HumanPlayer)
        self.assertEqual(p1, game.player_piece_dict['X'])
        self.assertEqual(p2, game.player_piece_dict['O'])

    def test_make_move_in_occupied_square(self):
        """
        Trying to place a piece in an occupied square should throw a runtime exception.
        """
        game = Game(Player, Player)
        game.make_move(game.player1, 5)
        self.assertRaises(RuntimeError, game.make_move, game.player1, 5)

    def test_make_move_in_empty_square(self):
        """
        Making a move should set that square in the board to the specified player's piece.
        """
        game = Game(Player, Player)
        self.assertEqual(None, game.board.get_square(5))
        game.make_move(game.player1, 5)
        self.assertEqual(game.player1.piece, game.board.get_square(5))

    def test_get_by_piece(self):
        """
        Calling this function with a player's piece should return the player object with that piece. The first player's
        piece should be an 'X' and the second player's piece should be an 'O'.
        """
        game = Game(Player, Player)
        p1 = game.player1
        p2 = game.player2
        self.assertEqual(p1, game.get_by_piece('X'))
        self.assertEqual(p2, game.get_by_piece('O'))


class PlayerTest(TestCase):
    def test_init(self):
        """
        After initialization, the player's piece should be set to the one it was called with.
        """
        game = Game(Player, Player)
        player = game.player1
        self.assertEqual('X', player.piece)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from main import generate_board, move_player

class TestSimpleGame(unittest.TestCase):

    def test_board_initialization(self):
        board, start_row, start_col, end_row, end_col = generate_board()
        self.assertEqual(len(board), 5)
        self.assertEqual(start_row, 0)
        self.assertEqual(start_col, 0)
        self.assertEqual(end_row, 4)
        self.assertEqual(end_col, 4)

    def test_player_movement(self):
        board, start_row, start_col, end_row, end_col = generate_board()
        board[1][0] =  '_'
        current_row, current_col = move_player(board, 's', 0, 0,)
        self.assertNotEqual(start_row, current_row)
        self.assertEqual(start_col, current_col)

    def test_reaching_the_end(self):
        board , _, _, end_row, end_col = generate_board()
        board[4][3] =  '_'
        current_row, current_col = move_player(board, 's', 3, 3)
        self.assertEqual(current_row, 4)
        self.assertEqual(current_col, 3)

    def test_avoiding_obstacle(self):
        board, start_row, start_col, end_row, end_col = generate_board()
        board[0][1] = 'X'
        current_row, current_col = move_player(board, 'd', 0, 0)
        self.assertEqual(current_row, 0)
        self.assertEqual(current_col, 0)

    def test_attempt_to_move_out_of_bounds(self):
        board , _, _, end_row, end_col = generate_board()
        current_row, current_col = move_player(board, 's', 4, 4)
        self.assertEqual(current_row, 4)
        self.assertEqual(current_col, 4)

    def test_obstacle_count(self):
        board , _, _, end_row, end_col = generate_board()
        obstacle_count = sum(row.count('X') for row in board)
        self.assertEqual(obstacle_count, 3, "Liczba przeszkód na planszy powinna być równa 3")

    @patch('builtins.input', return_value='x')
    def test_invalid_input(self, mock_input):
        board, start_row, start_col, end_row, end_col = generate_board()
        new_row, new_col = move_player(board, 'x', start_row, start_col)
        self.assertEqual(start_row, new_row)
        self.assertEqual(start_col, new_col)

if __name__ == "__main__":
    unittest.main()